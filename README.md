# Voice Assistant Project

## Overview

This Python project implements a basic voice assistant that recognizes voice commands, performs actions, and manages tasks. The voice assistant uses speech recognition, text-to-speech conversion, and task management functionalities.

## Features

- **Speech Recognition:** Captures voice commands through the microphone.
- **Text-to-Speech:** Converts response text into an audio file.
- **Task Management:** Allows users to add tasks and lists them.
- **Additional Actions:** Takes screenshots and opens Chrome to a specific URL.
- **Exit Command:** Allows the user to exit the program.

## Dependencies

- `speech_recognition`
- `gtts` (Google Text-to-Speech)
- `pydub`
- `pyautogui`

Install dependencies using:

```bash
pip install SpeechRecognition gtts pydub pyautogui
Configuration
Ensure correct configuration of the following:

FFmpeg: Set the correct path to the FFmpeg binary in the ffmpeg_path variable.
Usage
Run the main() function to initiate the voice assistant.
Use voice commands prefixed with the keyword "siri" for the assistant to recognize.
Example Commands:
"smj, add a task": Adds a task to the list.
"smj, list tasks": Lists the current tasks.
"smj, take a screenshot": Captures a screenshot.
"smj, open chrome": Opens Chrome to a specific URL.
"smj, exit": Terminates the voice assistant.
Notes
Ensure paths to Python, the main script, and FFmpeg are correctly specified.
Handle KeyboardInterrupt (Ctrl+C) to exit the program gracefully.
