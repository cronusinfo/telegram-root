import os
import asyncio
from telegram import Bot, InputFile
from telegram import Bot

async def download_video():
    bot = Bot("###")    # your API goes here
    message = await bot.get_chat_member("############", 10) # video user, id
    file_id = message.video.file_id
    file_path = await bot.download_file(file_id)
    destination_path = (r"#############################") # directory 
    with open(destination_path, "wb") as file:
        file.write(file_path)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_video())

if __name__ == "__main__":
    main()
    
    