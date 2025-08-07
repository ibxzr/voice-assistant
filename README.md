# voice-assistant
Python voice assistant using OpenAI Whisper for speech-to-text, GPT-4o for responses, and pyttsx3 for text-to-speech.
# Voice Assistant 🎙️🤖 
This is a simple Python-based voice assistant that records your voice, transcribes it using OpenAI Whisper, sends it to GPT-4o for a response, and reads the response out loud using pyttsx3.
## 🛠️ Features 
- Records audio through your microphone - Transcribes audio to text using OpenAI Whisper - Gets response from GPT-4o (OpenAI) - Speaks the reply using a selected voice (TTS via pyttsx3) ## 📦 Requirements - Python 3.8+ - openai - pyttsx3 - pyaudio - wave Install requirements with: pip install openai pyttsx3 pyaudio > On Windows, if pyaudio fails to install, use: pip install pipwin then pipwin install pyaudio
## 🔑 Setup 
Replace "YOUR_API_KEY" with your actual OpenAI API key in the script. client = openai.OpenAI(api_key="YOUR_API_KEY")
## ▶️ Usage 
Just run the script: python voice_assistant.py It will: 1. Record your voice for 5 seconds. 2. Transcribe it. 3. Generate a reply. 4. Speak it back to you. 
## 🌐 Language
Support - By default, the assistant speaks English. - You can change the system prompt and voice settings to support Arabic or any other language.
## 🧠 Model
- Whisper-1 for transcription - GPT-4o for conversation ---
Created by Renad faydh
