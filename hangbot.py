from discord.ext import commands
from asyncio import sleep
import game
from utils import literals as LITS 
from utils import api

bot = commands.Bot(command_prefix='$')
hangman_game = game.HangmanGame()


@bot.event
async def on_ready() -> None:
    print('logged in')


@bot.listen('on_message')
# https://discordpy.readthedocs.io/en/latest/faq.html#why-does-on-mes
# sage-make-my-commands-stop-working
async def new_message(message) -> None:
    if message.author == bot.user:  # prevent the bot from responding to himself
        return


# ------ * Bot commands * ------ #
@bot.command()
async def start_game(ctx) -> None:
    """Initialize a game and wait for users.
    Usage: $start_game
    """
    hangman_game.game_on = True
    await ctx.message.channel.send(LITS.GAME_BOT['GAME_TIMEOUT_WARN'])
    await sleep(10) # SUPPOSED TO WAIT 60s $$$$$$$$$$$

    if hangman_game.players == {}:
        hangman_game.reset()
        return await ctx.message.channel.send(LITS.GAME_BOT['GAME_ABORT'])
    else:  # init the game
        hangman_game.secret_word = api.get_random_word()
        definition = api.get_word_definition(
            hangman_game.secret_word)  # to delete
        await ctx.message.channel.send(LITS.GAME_BOT['GAME_GOING'])
        await ctx.message.channel.send(definition)  # to delete


@bot.command()
async def moi(ctx) -> None:
    """Add user to the game.
    Usage : $moi
    """
    if hangman_game.game_on == False:
        await ctx.message.channel.send(LITS.GAME_BOT['GAME_FIRST'])
        return

    user = ctx.author
    hangman_game.players[user.id] = (user.name, 0)
    await ctx.message.channel.send('oker {0}'.format(ctx.author.name))
