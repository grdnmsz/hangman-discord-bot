from discord.ext import commands
import game

from utils import api

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
@bot.command()
async def start_game(ctx) -> None:
    """Initialize a game and wait for users.
    Usage: $start_game
    """
    hangman_game.secret_word = api.get_random_word()
    definition = api.get_word_definition(hangman_game.secret_word) # to delete
    await ctx.message.channel.send(definition) # to delete 


@bot.command()
async def moi(ctx) -> None:
    """Add user to the game.
    Usage : $moi
    """
    if hangman_game.game_on == False:
        await ctx.message.channel.send("Start a game first (cf. $start_game)")
        return

    user = ctx.author
    hangman_game.players.push({user.id: (user.name, 0)})
    await ctx.message.channel.send('oker {0}'.format(ctx.author.name))
