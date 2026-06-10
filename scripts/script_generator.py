from google import genai
from dotenv import load_dotenv
import os
import time

# Load .env file
load_dotenv("../.env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

topic = input("Enter topic: ")

prompt = f"""
Write a YouTube Shorts voiceover script on:

{topic}

Rules:

- Output ONLY the spoken narration.
- Do NOT include:
  - titles
  - scene descriptions
  - timestamps
  - markdown
  - bullet points
  - Speaker:
  - Visual:
  - explanations
  - notes

Requirements:

- 45 seconds
- Hook in first sentence
- Simple English
- Short sentences
- Conversational style
- End with one practical tip

Return ONLY plain text.
"""

# Retry if Gemini is busy
for attempt in range(5):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        break

    except Exception as e:
        print("Gemini busy, retrying in 10 seconds...")
        time.sleep(10)

script = response.text

with open("script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("\nScript generated successfully!\n")
print(script)