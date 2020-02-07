from discord.ext import commands

description = 'This is a simple bot for testing features'

bot = commands.Bot(command_prefix='!', description=description)#prefix to all commands

#comand exsample
# @bot.command()
# async def test(ctx):
#     await dothings

async def echo(ctx, arg):
    await ctx.send(arg)

bot.run('token') #important!