# Jarvis-project

A simple offline/online voice assistant implemented in Python. Jarvis listens for the wake word ("jarvis"), accepts spoken commands, can open websites, play music links, read headlines, and forward[...]



## Features
- Wake-word detection using the microphone.
- Speech-to-text (Google Web Speech via speech_recognition).
- Text-to-speech with gTTS and playback via pygame.
- Open common websites (Google, YouTube, Facebook, LinkedIn).
- Play music links from a simple music library.
- Read top headlines using NewsAPI.
- Forward open-ended questions to the Google GenAI (Gemini) API for conversational responses.

## Prerequisites
- Python 3.8+
- Microphone and speakers configured on your system
- Network access to use online services (Google speech recognition, NewsAPI, Gemini)
- Accounts/API keys:
  - Google GenAI / Gemini API key
  - NewsAPI key (https://newsapi.org/)

## Recommended Python packages
- speechrecognition
- pyttsx3 (optional if you prefer offline TTS)
- gTTS
- pygame
- requests
- google-genai (or official package name for Gemini client)
- python-dotenv (optional, for environment variable support)

You can install most of these with:
pip install speechrecognition pyttsx3 gTTS pygame requests python-dotenv

(If you find an official pip name for the Gemini client, add it to the list.)

## Setup and Installation

1. Clone the repo:
   git clone https://github.com/Rugved1012/Jarvis-project.git
   cd Jarvis-project

2. (Optional) Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate     # Windows

3. Install dependencies:
   pip install -r requirements.txt
   If requirements.txt is not present, install the packages listed above manually.

4. Configure API keys
   - Do NOT store API keys directly in source code.
   - Create a `.env` file or export environment variables:
     export GEMINI_API_KEY="your_gemini_api_key"
     export NEWSAPI_KEY="your_newsapi_key"
   - Alternatively, update the code to read from environment variables (examples below).

5. Run Jarvis:
   python main.py

## How to configure keys in code (recommended)
Example (use python-dotenv or os.environ):
```python
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment variables

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
```

## Acknowledgements
This project was developed with reference to CodeWithHarry's tutorial/code. Thank you to CodeWithHarry for the helpful examples and explanations.
