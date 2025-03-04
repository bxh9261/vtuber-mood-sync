import os
from transcribe import transcribe_audio
from analyze_mood import analyze_mood
from generate_video import create_video
from config import MOOD_OPTIONS

def find_audio_file(directory="audio"):
    """Find the first .mp3 or .wav file in the given directory."""
    for file in os.listdir(directory):
        if file.endswith((".mp3", ".wav")):
            return os.path.join(directory, file)
    return None  # No valid audio file found

def get_user_moods():
    print("Available moods:", ", ".join(MOOD_OPTIONS.keys()))
    selected_moods = input("Enter the moods you want (comma-separated): ").lower().split(", ")
    
    valid_moods = {mood: MOOD_OPTIONS[mood] for mood in selected_moods if mood in MOOD_OPTIONS}
    
    if len(valid_moods) < 2:
        print("You must select at least two moods.")
        return get_user_moods()
    
    return valid_moods

if __name__ == "__main__":
    # Find an audio file in the "audio/" directory
    audio_file = find_audio_file()

    if not audio_file:
        print("No .mp3 or .wav file found in the 'audio' directory. Please add an audio file.")
        exit(1)

    print(f"Found audio file: {audio_file}")

    # Get user-selected moods
    user_moods = get_user_moods()

    # Transcribe audio to text
    transcript = transcribe_audio(audio_file)

    # Analyze moods in the transcript
    mood_map = analyze_mood(transcript, user_moods)

    # Print each sentence with its detected mood
    print("\nSentence Mood Analysis:")
    for sentence, mood in mood_map.items():
        print(f"[{mood.upper()}] {sentence}")

    # Generate video with mood-based avatars
    mood_images = {mood: f"assets/{mood}.png" for mood in user_moods.keys()}
    output_video = "output/final_video.mp4"

    create_video(audio_file, mood_map, mood_images, output_video)

    print(f"Video generated successfully! Check '{output_video}'.")
