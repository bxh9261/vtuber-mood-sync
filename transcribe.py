import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    audio_file = "audio/speech.wav"
    transcript = transcribe_audio(audio_file)
    print("Transcript:", transcript)
