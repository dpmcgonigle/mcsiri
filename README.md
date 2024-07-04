#   McSiri

##  Contents
- [Description](#description)
- [Installation](#installation)
    - [Requirements](#requirements)
- [Usage](#usage)
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

[Back to Top](#ecole-core)

##  Usage

### Command Line Interface

Try `python mcsiri/cli.py --help` for more information.

You will need to pass the OPENAI_API_KEY by one of the following methods:
1. Use the --openai-api-key flag
2. Use an environment variable, i.e. `export OPENAI_API_KEY=xxxx python mcsiri/cli.py [ARGS]`

