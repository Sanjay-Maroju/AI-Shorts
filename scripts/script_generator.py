from google import genai
import os

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

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

script = response.text

with open("script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print(script)