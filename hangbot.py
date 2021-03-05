from discord.ext import commands
import game

bot = commands.Bot(command_prefix='$')
hangman_game = game.HangmanGame({})


@bot.event
async def on_ready() -> None:
    print('logged in')


@bot.listen('on_message')
# https://discordpy.readthedocs.io/en/latest/faq.html#why-does-on-message-make-my-commands-stop-working
async def new_message(message) -> None:
    if message.author == bot.user:  # prevent the bot from responding to himself
        return

# ------ * Bot commands * ------ #
"""
@bot.command()
async def help_(ctx) -> None:
    message_help = hangman_game.help()
    await ctx.message.channel.send(message_help)
"""


@bot.command()
async def start_game() -> None:
    """Initialize a game and wait for users.
    Usage: $start_game"""


@bot.command()
async def moi(ctx) -> None:
    """Add user to the game.
    Usage : $moi
    """
    if hangman_game.game_on != False:
        await ctx.message.channel.send("Start a game first")
        return

    # ctx.author.id
    await ctx.message.channel.send('oker {0}'.format(ctx.author.name))
