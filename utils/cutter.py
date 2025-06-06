
from moviepy.editor import VideoFileClip
import os

def cut_clips(video_path, matches, output_dir="output_clips"):
    os.makedirs(output_dir, exist_ok=True)
    clip_paths = []

    for i, m in enumerate(matches):
        clip = VideoFileClip(video_path).subclip(m["start"], m["end"])
        out_path = os.path.join(output_dir, f"clip_{i+1}.mp4")
        clip.write_videofile(out_path, codec="libx264", audio_codec="aac", verbose=False, logger=None)
        clip_paths.append((m["script"], out_path))
    
    return clip_paths
