import ffmpeg
import os

def cut_clips(video_path, matches, output_dir="output_clips"):
    os.makedirs(output_dir, exist_ok=True)
    clip_paths = []

    for i, m in enumerate(matches):
        start = m["start"]
        duration = min(10, m["end"] - m["start"])  # đảm bảo tối đa 10s
        out_path = os.path.join(output_dir, f"clip_{i+1}.mp4")

        (
            ffmpeg
            .input(video_path, ss=start, t=duration)
            .output(out_path, codec='libx264', acodec='aac')
            .overwrite_output()
            .run(quiet=True)
        )
        clip_paths.append((m["script"], out_path))

    return clip_paths
