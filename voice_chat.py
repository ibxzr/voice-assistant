import openai
import pyaudio
import wave
import pyttsx3


client = openai.OpenAI(api_key="API KEY")

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
print("\n🔊 Available voices:")
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name} - {voice.id}")

selected_voice_index = 1  
if selected_voice_index < len(voices):
    engine.setProperty('voice', voices[selected_voice_index].id)
else:
    print("⚠️ الصوت المختار غير متوفر. سيتم استخدام الصوت الافتراضي.")

# إعدادات التسجيل
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "recorded.wav"

def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("🎙️ Recording...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("🛑 Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_audio():
    with open(WAVE_OUTPUT_FILENAME, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

def chat_with_gpt(user_input):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def speak(text):
    engine.say(text)
    engine.runAndWait()

def voice_assistant():
    record_audio()
    user_text = transcribe_audio()
    print(f"👤 You said: {user_text}")
    gpt_response = chat_with_gpt(user_text)
    print(f"🤖 Assistant: {gpt_response}")
    speak(gpt_response)

voice_assistant()