from discord.ext import commands

description = 'This is a simple bot for testing features'

bot = commands.Bot(command_prefix='!', description=description)#prefix to all commands

commands = [
    "!help - display all commands",
    "!echo 'arg' - return arg"
]

#comand exsample
# @bot.command()
# async def test(ctx):
#     await dothings

@bot.command()
async def help(ctx):
    for command in commands:
        await ctx.send(command)

@bot.command()
async def echo(ctx, arg):
    ctx.send(arg)

bot.run('token') #important!