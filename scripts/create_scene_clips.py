
import json
import subprocess

# Load subtitle timestamps
with open("../subtitles/voice.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["segments"]

# Map subtitle segments to scenes
scene_ranges = [
    (0, 1),
    (2, 3),
    (4, 5),
    (6, 7),
    (8, 8),
    (9, 9),
    (10, 10)
]

fps = 25

for i, (start_idx, end_idx) in enumerate(scene_ranges, start=1):

    if end_idx < len(segments)-1:
        duration = segments[end_idx+1]["start"] - segments[start_idx]["start"]
    else:
        duration = segments[end_idx]["end"] - segments[start_idx]["start"]

    frames = round(duration * fps)

    print(f"Creating clip{i}.mp4")

    command = [
        "ffmpeg",
        "-y",

        "-loop", "1",
        "-framerate", str(fps),
        "-i", f"../assets/scene{i}.png",

        "-vf", "scale=1080:1920",

        "-frames:v", str(frames),

        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",

        f"../video/clip{i}.mp4"
    ]

    subprocess.run(command)

print("All clips created successfully!")

