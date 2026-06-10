from google import genai
from dotenv import load_dotenv
import os
import time

# Load .env
load_dotenv("../.env")

# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Read the script
with open("script.txt", "r", encoding="utf-8") as f:
    script = f.read()

prompt = f"""
Convert the following YouTube Shorts narration into exactly 8 cinematic scenes.

Rules:

- One scene per line.
- No numbering.
- No explanations.
- Maintain the same character throughout.
- Young Indian college student.
- Ultra realistic.
- DSLR quality.
- Cinematic lighting.
- Detailed environments.
- Dynamic camera angles.
- Strong emotions.
- Vertical 9:16.
- Suitable for YouTube Shorts.
- Avoid repetitive close-up shots.
- Use a mix of wide shots, medium shots, over-the-shoulder shots and close-ups.

Narration:

{script}
"""

# Retry up to 5 times if Gemini is busy
for attempt in range(5):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        scene_prompts = response.text

        with open("scene_prompts.txt", "w", encoding="utf-8") as f:
            f.write(scene_prompts)

        print("\nScene prompts generated successfully!\n")
        print(scene_prompts)

        break

    except Exception as e:
        print(f"Attempt {attempt+1}/5 failed.")
        print(e)

        if attempt < 4:
            print("Retrying in 10 seconds...\n")
            time.sleep(10)
        else:
            print("Failed after 5 attempts.")