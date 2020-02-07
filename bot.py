from discord.ext import commands

bot = commands.Bot(command_prefix='!')#prefix to all commands

#comand exsample
# @bot.command()
# async def test(ctx):
#     await dothings

async def echo(ctx, arg):
    await ctx.send(arg)

bot.run('token') #important!