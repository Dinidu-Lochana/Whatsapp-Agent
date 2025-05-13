from vosk import Model, KaldiRecognizer
import pyaudio
import json

def transcribe_voice():
    # Vosk model for speech recognition
    model = Model("vosk-model-small-en-us-0.15")  
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()             # Initialize the microphone
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000,
                      input=True, frames_per_buffer=8192)
    print("🎤 Speak something...")

    stream.start_stream()       # Start the stream for continuous microphone input
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            break

    stream.stop_stream()        # Stop the stream and off the microphone input
    stream.close()
    mic.terminate()

    text = json.loads(result).get("text", "")
    print("📝 Transcribed Text:", text)
    return text