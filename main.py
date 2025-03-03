from transcribe import transcribe_audio
from analyze_mood import analyze_mood
from generate_video import create_video
from config import MOOD_OPTIONS

def get_user_moods():
    print("Available moods:", ", ".join(MOOD_OPTIONS.keys()))
    selected_moods = input("Enter the moods you want (comma-separated): ").lower().split(", ")
    
    valid_moods = {mood: MOOD_OPTIONS[mood] for mood in selected_moods if mood in MOOD_OPTIONS}
    
    if len(valid_moods) < 2:
        print("You must select at least two moods!")
        return get_user_moods()
    
    return valid_moods

if __name__ == "__main__":
    # Step 1: Get user-selected moods
    user_moods = get_user_moods()

    # Step 2: Transcribe audio
    audio_file = "audio/speech.wav"
    transcript = transcribe_audio(audio_file)

    # Step 3: Analyze moods
    mood_map = analyze_mood(transcript, user_moods)

    # Step 4: Generate video
    mood_images = {mood: f"assets/{mood}.png" for mood in user_moods.keys()}
    create_video(audio_file, mood_map, mood_images, "output/final_video.mp4")

    print("🎬 Video generated successfully! Check 'output/final_video.mp4'")

