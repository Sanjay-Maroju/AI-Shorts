import subprocess

command = [
    "ffmpeg",
    "-y",

    # Video with subtitles and voice
    "-i", "../output/final_short_subtitled.mp4",

    # Background music (loop if necessary)
    "-stream_loop", "-1",
    "-i", "../audio/bgm.mp3",

    # Mix audio
    "-filter_complex",
    "[0:a]volume=1[a0];"
    "[1:a]volume=0.10[a1];"
    "[a0][a1]amix=inputs=2:duration=first[a]",

    # Keep video from first input
    "-map", "0:v",
    "-map", "[a]",

    # Output settings
    "-c:v", "copy",
    "-c:a", "aac",
    "-shortest",

    "../output/final_short_music.mp4"
]

subprocess.run(command)

print("Background music added successfully!")