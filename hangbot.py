from discord.ext import commands
import game

bot = commands.Bot(command_prefix='$')
hangmanGame = game.HangmanGame({})

@bot.event
async def on_ready():
    print('logged in')


@bot.listen('on_message') 
# https://discordpy.readthedocs.io/en/latest/faq.html#why-does-on-message-make-my-commands-stop-working
async def new_message(message):
    if message.author == bot.user:  # prevent the bot from responding to himself
        return
    await message.channel.send('tu m\'en diras tant')


# ------ * Bot commands * ------ #

@bot.command()
async def start_game():
    """Initialize a game and wait for users."""


@bot.command()
async def moi(ctx):
    """Add user to the game."""
    print(ctx.author.id)
