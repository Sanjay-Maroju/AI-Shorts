import json
import subprocess

# Load subtitle timestamps
with open("../subtitles/voice.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["segments"]

command = ["ffmpeg"]

# Add images with durations from voice.json
scene_ranges = [
    (0,1),
    (2,3),
    (4,5),
    (6,7),
    (8,9),
    (10,11),
    (12,12),
    (13,13)
]

for i, (start_idx, end_idx) in enumerate(scene_ranges, start=1):

    duration = (
        segments[end_idx]["end"]
        - segments[start_idx]["start"]
    )

    command.extend([
        "-loop", "1",
        "-t", str(duration),
        "-i", f"../assets/scene{i}.png"
    ])

# Audio
command.extend([
    "-i", "../audio/voice.mp3"
])

# Build filter_complex
filter_complex = ""

for i in range(8):
    filter_complex += f"[{i}:v]scale=1080:1920[v{i}];"

concat_inputs = "".join([f"[v{i}]" for i in range(8)])

filter_complex += f"{concat_inputs}concat=n=8:v=1:a=0[v]"

command.extend([
    "-filter_complex", filter_complex,
    "-map", "[v]",
    "-map", "8:a",
    "-c:v", "libx264",
    "-c:a", "aac",
    "-pix_fmt", "yuv420p",
    "-shortest",
    "-y",
    "../output/final_short.mp4"
])

subprocess.run(command)