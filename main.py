import hangbot
import os

from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    bot = hangbot.bot
    bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()