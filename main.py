from hangbot import HangmanBot
import os

from dotenv import load_dotenv

if __name__ == '__main__':
  load_dotenv()
  DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
  print("coucou")
  bot = HangmanBot()
  bot.run(DISCORD_TOKEN)