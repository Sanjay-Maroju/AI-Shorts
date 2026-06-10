import subprocess

print("\nGenerating script...")
subprocess.run(["python", "script_generator.py"])

print("\nGenerating voice...")
subprocess.run(["python", "voice.py"])

print("\nGenerating scene prompts...")
subprocess.run(["python", "scene_generator.py"])

print("\nGenerating images...")
subprocess.run(["python", "image_generator.py"])

print("\nCreating video...")
subprocess.run(["python", "ffmpeg.py"])

print("\nBurning subtitles...")
subprocess.run(["python", "burn_subtitles.py"])

print("\nAdding background music...")
subprocess.run(["python", "add_bgm.py"])

print("\nDone! Upload-ready video created.")