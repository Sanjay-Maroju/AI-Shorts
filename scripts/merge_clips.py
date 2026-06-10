
import subprocess

command = [
    "ffmpeg",
    "-y",

    "-i", "../video/clip1.mp4",
    "-i", "../video/clip2.mp4",
    "-i", "../video/clip3.mp4",
    "-i", "../video/clip4.mp4",
    "-i", "../video/clip5.mp4",
    "-i", "../video/clip6.mp4",
    "-i", "../video/clip7.mp4",

    "-filter_complex",
    "[0:v][1:v][2:v][3:v][4:v][5:v][6:v]concat=n=7:v=1:a=0[v]",

    "-map", "[v]",

    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",

    "../video/merged.mp4"
]

subprocess.run(command)

print("Merged successfully!")
