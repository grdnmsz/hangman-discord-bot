from discord import Client
from discord.ext import commands

class HangmanBot(commands.Bot, Client):
  def __init__(self):
    super().__init__(self)

  async def on_ready(self):
    print('joined!')

  async def on_message(self, message):
    if message.author == self.user: # prevent the bot to respond to himself
        return
    await message.channel.send('je ne sais dire que ça')
