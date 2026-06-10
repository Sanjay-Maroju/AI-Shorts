import subprocess

command = [
    "ffmpeg",

    # Images (6.5 sec each)
    "-loop", "1", "-t", "6.5", "-i", "../assets/scene1.png",
    "-loop", "1", "-t", "6.5", "-i", "../assets/scene2.png",
    "-loop", "1", "-t", "6.5", "-i", "../assets/scene3.png",
    "-loop", "1", "-t", "6.5", "-i", "../assets/scene4.png",
    "-loop", "1", "-t", "6.5", "-i", "../assets/scene5.png",
    "-loop", "1", "-t", "6.5", "-i", "../assets/scene6.png",
    "-loop", "1", "-t", "6.5", "-i", "../assets/scene7.png",
    "-loop", "1", "-t", "6.5", "-i", "../assets/scene8.png",

    # Audio
    "-i", "../audio/voice.mp3",

    # Resize all images and concatenate
    "-filter_complex",
    "[0:v]scale=1080:1920[v0];"
    "[1:v]scale=1080:1920[v1];"
    "[2:v]scale=1080:1920[v2];"
    "[3:v]scale=1080:1920[v3];"
    "[4:v]scale=1080:1920[v4];"
    "[5:v]scale=1080:1920[v5];"
    "[6:v]scale=1080:1920[v6];"
    "[7:v]scale=1080:1920[v7];"
    "[v0][v1][v2][v3][v4][v5][v6][v7]concat=n=8:v=1:a=0[v]",

    "-map", "[v]",
    "-map", "8:a",

    "-c:v", "libx264",
    "-c:a", "aac",
    "-pix_fmt", "yuv420p",

    "../output/final_short.mp4"
]

subprocess.run(command)