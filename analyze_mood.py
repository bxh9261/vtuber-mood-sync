import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from config import MOOD_OPTIONS

nltk.download('vader_lexicon')

def analyze_mood(text, selected_moods):
    sia = SentimentIntensityAnalyzer()
    sentences = text.split(". ")  # Split text into sentences
    mood_map = []

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
        
        mood_map.append((sentence, best_match))

    return mood_map

if __name__ == "__main__":
    # Example usage
    sample_text = "Hello everyone! I can't believe this right now. This is terrible."
    user_moods = {mood: MOOD_OPTIONS[mood] for mood in ["happy", "angry", "sad", "neutral"]}  # User selects 4 moods
    mood_result = analyze_mood(sample_text, user_moods)
    
    for sentence, mood in mood_result:
        print(f"[{mood}] {sentence}")
