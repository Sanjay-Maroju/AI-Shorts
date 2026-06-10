import os

print("Generating script...")
os.system("python script_generator.py")

print("Generating voice...")
os.system("python voice.py")

print("Generating subtitles...")
os.system("python -m whisper ../audio/voice.mp3 --model base")

print("DONE!")