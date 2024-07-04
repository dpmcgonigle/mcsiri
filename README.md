#   McSiri

##  Contents
- [Description](#description)
- [Installation](#installation)
    - [Requirements](#requirements)
- [Usage](#usage)
    - [OpenAI API Key](#openai-api-key)
    - [Command Line Interface](#command-line-interface)

##  Description

This program integrates speech recognition with an LLM interface to test audio chatbot functionality.

##  Installation

Install McSiri package with all dependencies:
```bash
cd /path/to/mcsiri  # dir with setup.py
pip install .
```

Alternatively, you can install the dependencies directly:
```bash
cd /path/to/mcsiri  # dir with setup.py
pip install -r requirements.txt
```

### Requirements

PortAudio is a requirement of pyaudio.  If you try to install the requirements without PortAudio, it should fail. 

[PortAudio](https://portaudio.com/)

### Development Requirements

For developing, testing, formatting and linting:

`pip install -r requirements-dev.txt`

[Back to Top](#mcsiri)

##  Usage

### OpenAI API Key

This program requires an OPENAI_API_KEY. You can include it with one of the following methods:
1. Use the --openai-api-key CLI argument to cli.py
2. Use an environment variable, i.e. `export OPENAI_API_KEY=xxxx python mcsiri/cli.py [ARGS]`

### Command Line Interface

You can run this program with either of the following:
- `python mcsiri/cli.py`
- `mcsiri`

Use --stream-logs to see logging

Try `python mcsiri/cli.py --help` for more information.

[Back to Top](#mcsiri)
