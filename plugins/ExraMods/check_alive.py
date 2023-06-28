import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("சாகவில்லை ஆனால் இன்னும் இங்கேயே இருக்கிறாய்.. உனக்கு இப்போது என் மீது காதல் இல்லை. நல்லது.. நீ முன்பு போல் இல்லை /start")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
