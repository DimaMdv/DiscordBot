from discord.ext import commands
from random import randint as rint

description = 'This is a simple bot for testing features' #description of the bot
commands_pref = '!' #commands prefix !/$/'/'/@/'#'

bot = commands.Bot(command_prefix=commands_pref, description=description)#prefix to all commands

commands = [
    'help - display all commands',
    'echo "arg" - return arg',
    'dice "number" - return random number betwen 1 and "number"'
]

#comand exsample
# @bot.command()
# async def test(ctx):
#     await dothings

@bot.command()
async def help(ctx):
    for command in commands:
        await ctx.send(commands_pref + command)

@bot.command()
async def dice(ctx, arg:int):
    try:
        await ctx.send(rint(1, arg))
    except Exception:
        await ctx.send('Oops, seems its not a number!')

@bot.command()
async def echo(ctx, arg):
    ctx.send(arg)

bot.run('token') #important!