import subprocess

command = [
    "ffmpeg",
    "-y",

    "-i", "../video/merged.mp4",
    "-i", "../audio/voice.mp3",

    "-map", "0:v",
    "-map", "1:a",

    "-c:v", "copy",
    "-c:a", "aac",

    "-shortest",

    "../output/final_short.mp4"
]

subprocess.run(command)

print("Voice added successfully!")