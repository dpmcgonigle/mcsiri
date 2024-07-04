import os
import time
import logging
import pyaudio
import argparse
import playsound
import traceback
from gtts import gTTS
from openai import OpenAI
import speech_recognition as sr

from mcsiri.logger import setup_logger


logger = logging.getLogger(__name__)
datadir = os.path.join(os.path.dirname(__file__), "data")
audiofile = os.path.join(datadir, "welcome1.mp3")


def get_args() -> argparse.Namespace:
    """Get command-line arguments.

    Raises:
        ValueError: If OpenAI API key is not provided

    Returns:
        argparse.Namespace: Command-line arguments to run program
    """
    parser = argparse.ArgumentParser(description="Chat with Chauncey")
    parser.add_argument("--openai-api-key", type=str, help="OpenAI API key; if not provided, will use OPENAI_API_KEY env var")
    parser.add_argument("--lang", type=str, default="en", help="Language (default: en)")
    #   Logging
    parser.add_argument("--stream-logs", action="store_true", help="Stream logs to stdout")
    parser.add_argument("--log-level", type=str, default="INFO", help="Log level (default: INFO)")
    args = parser.parse_args()

    if not args.openai_api_key:
        args.openai_api_key = os.getenv("OPENAI_API_KEY")
    if not args.openai_api_key:
        raise ValueError("OpenAI API key not provided")
    
    return args


def configure_logging(args: argparse.Namespace) -> None:
    """Configure logging.

    Args:
        args (argparse.Namespace): Command-line arguments
    """
    #   Set up logger
    log_file = f"{os.path.splitext(__file__)[0]}.log"
    setup_logger(stream_logs=args.stream_logs, log_level=args.log_level, log_file=log_file)


def main() -> None:
    """Main function to run program.

    Args:
        args (argparse.Namespace): Command-line arguments
    """
    args = get_args()
    configure_logging(args)

    client = OpenAI(api_key = args.openai_api_key)
    logger.info(f"STARTING CHAUNCEY, press Ctrl+C to stop.")

    while True:

        #   Keyboard interrupt to stop (Ctrl+C)
        try:

            def get_audio():
                r = sr.Recognizer()
                with sr.Microphone(device_index=1) as source:
                    logger.info(f"Started listening")
                    audio = r.listen(source)
                    said: str = ""
                
                    try:
                        said = r.recognize_google(audio, language="en-US")
                        logger.info(f"User: {said}")
                        print(said)
                    
                        if "chauncey" in said.lower():
                            completion = client.chat.completions.create(
                                model="gpt-3.5-turbo", messages=[{"role": "user", "content": said}]
                            )
                            text = completion.choices[0].message.content
                            speech = gTTS(text=text,lang=args.lang,slow=False,tld="com.au")
                            speech.save(audiofile)
                            playsound.playsound(audiofile)
                        
                    except sr.exceptions.UnknownValueError:
                        logger.warning("Google Speech Recognition could not understand the audio")
                    except sr.exceptions.RequestError:
                        logger.warning("Could not request results from Google Speech Recognition service")
                    except Exception as err:
                        logger.error(f"Unknown Error: {err}")
                        traceback.print_exc()
                    
                return said
        
            get_audio()

            #   Sleep for a bit
            time.sleep(0.1)

        except KeyboardInterrupt:
            print("\n********\nQuit program? (y/n): ")
            ans = input()
            if ans.lower() in ["y", "yes"]:
                logger.info("Stopping Chauncey")
                break
            else:
                continue


if __name__ == "__main__":
    main()