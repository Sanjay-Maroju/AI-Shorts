import asyncio
import edge_tts

VOICE = "en-US-GuyNeural"

with open("script.txt", "r", encoding="utf-8") as f:
    TEXT = f.read()

OUTPUT_FILE = "../audio/voice.mp3"

async def main():
    print(TEXT)
    print("\nLength:", len(TEXT))
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

asyncio.run(main())