import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from config import MOOD_OPTIONS

nltk.download('vader_lexicon')

def analyze_mood(text, selected_moods):
    """Analyze the mood of each sentence in the text and return a dictionary."""
    sia = SentimentIntensityAnalyzer()
    sentences = text.split(". ")  # Split text into sentences
    mood_map = {}  # Store sentence -> mood as a dictionary

    for sentence in sentences:
        sentiment = sia.polarity_scores(sentence)['compound']
        
        # Find the best mood match from user's selected moods
        best_match = "neutral"
        best_diff = float("inf")

        for mood, (low, high) in selected_moods.items():
            if low <= sentiment <= high:
                best_match = mood
                break
            else:
                diff = min(abs(sentiment - low), abs(sentiment - high))
                if diff < best_diff:
                    best_diff = diff
                    best_match = mood

	# Weighting: Make neutral much more common
        if -0.3 <= sentiment <= 0.3 and "neutral" in selected_moods:
            best_match = "neutral"
        
        mood_map[sentence] = best_match  # Store as {sentence: mood}

    return mood_map  # Returns a dictionary

if __name__ == "__main__":
    # Example usage
    sample_text = "Hello everyone! I can't believe this right now. This is terrible."
    user_moods = {mood: MOOD_OPTIONS[mood] for mood in ["happy", "angry", "sad", "neutral"]}  # User selects 4 moods
    mood_result = analyze_mood(sample_text, user_moods)
    
    for sentence, mood in mood_result.items():
        print(f"[{mood}] {sentence}")

