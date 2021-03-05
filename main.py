import hangbot
import os

from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    bot = hangbot.bot
    bot.run(DISCORD_TOKEN)
