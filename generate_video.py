from moviepy.editor import *
import os

def create_video(audio_path, mood_map, image_dict, output_video):
    audio = AudioFileClip(audio_path)
    duration = audio.duration
    num_sentences = len(mood_map)

    clips = []
    start_time = 0

    for i, (fragment, mood) in enumerate(mood_map.items()):
        image_path = image_dict.get(mood, "assets/neutral.png")  # Default to neutral if mood missing
        img_clip = ImageClip(image_path, duration=duration / num_sentences).set_start(start_time)
        clips.append(img_clip)
        start_time += duration / num_sentences

    final_video = concatenate_videoclips(clips, method="compose").set_audio(audio)
    final_video.write_videofile(
    	output_video,
    	fps=24,
    	codec="libx264",
    	audio_codec="aac",
    	preset="slow",
    	ffmpeg_params=["-vf", "scale=trunc(iw/2)*2:ih", "-pix_fmt", "yuv420p"]
    )


if __name__ == "__main__":
    mood_map = [("Hello!", "happy"), ("I can't believe this!", "angry"), ("This is sad.", "sad")]
    mood_images = {
        "happy": "assets/happy.png",
        "angry": "assets/angry.png",
        "sad": "assets/sad.png",
        "neutral": "assets/neutral.png"
    }

    create_video("audio/speech.wav", mood_map, mood_images, "output/final_video.mp4")
