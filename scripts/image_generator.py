from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import time

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)

# Read prompts
with open("scene_prompts.txt", "r", encoding="utf-8") as f:
    prompts = [line.strip() for line in f.readlines() if line.strip()]

# Generate images
for i, prompt in enumerate(prompts, start=1):
    print(f"Generating scene{i}...")

    try:
        image = client.text_to_image(
            prompt,
            model="black-forest-labs/FLUX.1-schnell"
        )

        image.save(f"../assets/scene{i}.png")

        print(f"scene{i}.png saved")

        time.sleep(2)

    except Exception as e:
        print(f"Error generating scene{i}")
        print(e)

print("All images generated successfully!")