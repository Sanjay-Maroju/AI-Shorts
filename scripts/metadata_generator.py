from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Read script
with open("script.txt", "r", encoding="utf-8") as f:
    script = f.read()

prompt = f"""
Based on this YouTube Shorts script:

{script}

Generate:

1. A catchy YouTube title under 60 characters.
2. A SEO-friendly description (2-3 lines).
3. 10 relevant hashtags.

Return in this format:

TITLE:
...

DESCRIPTION:
...

HASHTAGS:
...
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

result = response.text

# Save complete metadata
with open("../upload/metadata.txt", "w", encoding="utf-8") as f:
    f.write(result)

# Extract sections
title = result.split("DESCRIPTION:")[0].replace("TITLE:", "").strip()

description = result.split("DESCRIPTION:")[1].split("HASHTAGS:")[0].strip()

hashtags = result.split("HASHTAGS:")[1].strip()

# Save separate files
with open("../upload/title.txt", "w", encoding="utf-8") as f:
    f.write(title)

with open("../upload/description.txt", "w", encoding="utf-8") as f:
    f.write(description)

with open("../upload/hashtags.txt", "w", encoding="utf-8") as f:
    f.write(hashtags)

print("Metadata saved successfully!")