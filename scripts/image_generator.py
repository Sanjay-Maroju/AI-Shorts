import requests
from urllib.parse import quote

# Read prompts
with open("scene_prompts.txt", "r", encoding="utf-8") as f:
    prompts = [line.strip() for line in f.readlines() if line.strip()]

for i, prompt in enumerate(prompts, start=1):
    print(f"Generating scene{i}...")

    url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

    img = requests.get(url).content

    with open(f"../assets/scene{i}.png", "wb") as f:
        f.write(img)

print("All images generated successfully!")