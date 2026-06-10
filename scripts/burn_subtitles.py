import subprocess

command = [
    "ffmpeg",
    "-y",
    "-i", "../output/final_short.mp4",
    "-vf", "subtitles=../subtitles/voice.srt",
    "../output/final_short_subtitled.mp4"
]

subprocess.run(command)

print("Subtitles added successfully!")