from discord.ext import commands
import discord
from random import randint as rint

description = 'This is a simple bot for testing features' #description of the bot
commands_prefix = '!' #commands prefix

bot = commands.Bot(command_prefix=commands_prefix, description=description)#prefix to all commands


@bot.event #calls when bot launched
async def on_ready(ctx):
    print('Logged in as')#logging in console
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    # await ctx.send('I\'m alive!')
    channel = bot.get_channel('chanel id')
    role = discord.utils.get(user.server.roles, name="rolename")
    message = await bot.send_message(channel, "message text")
    while True:
        reaction = await bot.wait_for_reaction(emoji="emoji", message=message)
        await bot.add_roles(reaction.message.author, role)



@bot.event #I dont know if its working, but I whant to belive so
async def on_member_join(ctx, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)

# @bot.event
# async def on_ready():
#     channel = bot.get_channel('549294402514976783')#DELETE CHANEL ID
#     role = discord.utils.get(user.server.roles, name="tester")#ROLENAME
#     message = await bot.send_message(channel, "React to me!")
#     while True:
#         reaction = await bot.wait_for_reaction(emoji=":penguin:", message=message)
#         await bot.add_roles(reaction.message.author, role)

@bot.command(description='return random number betwen 1 and an argument')
#description is seeing only on !help command
async def dice(ctx, arg:int):
    try:
        await ctx.send(rint(1, arg))
    except Exception:
        await ctx.send('Oops, seems its not a number!')

@bot.command(description='return "pong"')
async def ping(ctx):
    await ctx.send('pong')

@bot.command(description='reply with the same message')
async def echo(ctx, arg):
    await ctx.send(arg)


bot.run('token') #important!