# Voice Assistant 🎙️🤖

This is a simple Python-based voice assistant that records your voice, transcribes it using OpenAI Whisper, sends it to GPT-4o for a response, and reads the response out loud using pyttsx3.

## 🛠️ Features
- Records audio through your microphone
- Transcribes audio to text using OpenAI Whisper
- Gets response from GPT-4o (OpenAI)
- Speaks the reply using a selected voice (TTS via pyttsx3)

## 📷 Output Example
![Output Example](output_example.png)

## 📦 Requirements
- Python 3.8+
- openai
- pyttsx3
- pyaudio
- wave

Install requirements with:

```bash
pip install openai pyttsx3 pyaudio
On Windows, if pyaudio fails to install, use:
pip install pipwin
pipwin install pyaudio
##🔑 Setup

Replace "YOUR_API_KEY" with your actual OpenAI API key in the script.
