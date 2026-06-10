from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)

prompt = """
Ultra realistic young Indian college student using free public WiFi in a coffee shop,
cinematic lighting, highly detailed, DSLR quality, vertical 9:16
"""

image = client.text_to_image(
    prompt,
    model="black-forest-labs/FLUX.1-schnell"
)

image.save("../assets/test.jpg")

print("Image generated successfully!")