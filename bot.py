import os
import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create Telegram client (User or Bot)
# যদি বট টোকেন থাকে, বট মোডে চলবে, না হলে ইউজার মোডে।
if BOT_TOKEN:
    client = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
else:
    client = TelegramClient('user_session', API_ID, API_HASH)

async def main():
    print("Starting client...")

    await client.start(phone=PHONE)  # ফোন দিয়ে লগইন, যদি বট না হয়

    print("Client started!")

    # Simple event handler: যখন কেউ মেসেজ পাঠাবে
    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.respond('Hello! I am your bot/client.')
        print(f"Replied to {event.sender_id}")

    # যদি বট থাকে, নিচের কোড চালাও, না হলে ইউজার মোডে রেখে যেও

    # Run until disconnected
    print("Running until disconnected...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
