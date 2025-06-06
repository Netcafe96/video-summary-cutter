import os
import subprocess

def cut_clips(video_path, matches, output_dir="output_clips"):
    if os.path.exists(output_dir) and not os.path.isdir(output_dir):
        os.remove(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    clip_paths = []

    for i, m in enumerate(matches):
        start = m["start"]
        duration = min(10, m["end"] - m["start"])
        out_path = os.path.join(output_dir, f"clip_{i+1}.mp4")

        cmd = [
            "ffmpeg",
            "-y",
            "-ss", str(start),
            "-t", str(duration),
            "-i", video_path,
            "-c:v", "libx264",
            "-c:a", "aac",
            out_path
        ]

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            clip_paths.append((m["script"], out_path))
        except subprocess.CalledProcessError as e:
            print(f"Error cutting clip {i+1}: {e}")

    return clip_paths
