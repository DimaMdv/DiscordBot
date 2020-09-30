import discord
from discord.ext import commands
from discord.utils import get
from random import randint as rint

token = input("Enter the token:")  # just to not do it every time i lauch it
description = 'This is a simple bot for testing features'  # description of the bot
commands_prefix = '!'  # commands prefix

bot = commands.Bot(command_prefix=commands_prefix, description=description)


@bot.event
async def on_ready():  # calls when bot launched
    print("Im alive!")


@bot.event  # I dont know if its working, but I whant to belive so
async def on_member_join(ctx, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)


@bot.command(description='return random number betwen 1 and an argument')
# description is seeing only on !help command
async def dice(ctx, arg: int):
    try:
        await ctx.send(rint(1, arg))
    except Exception:
        await ctx.send('Oops, seems its not a number!')


@bot.command(description='return "pong"')
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}')


@bot.command(description='reply with the same message')
async def echo(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def kick(ctx, member: discord.Member, *, arg='Not provided'):
    await member.kick(reason=arg)
    await ctx.send(f'{member.mention} has been kick by {ctx.author.mention}. reason: {arg}')


@bot.command()
async def ban(ctx, member: discord.Member, *, arg='Not provided'):
    await member.ban(reason=arg)
    await ctx.send(f'{member.mention} has been banned by {ctx.author.mention}. reason: {arg}')


@bot.command()
async def kick(ctx, member: discord.Member, *, arg):
    await member.kick(reason=arg)


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(self, ctx, member: discord.Object):
    await ctx.guild.unban(member)
    await ctx.send(f'Ok unbanned user with ID {member.id}')


@bot.command()
async def clear(self, ctx, amount):
    total = await ctx.channel.purge(limit=amount)
    await ctx.send('done', delete_after=4)


@bot.command()
@commands.has_guild_permissions(mute_members=True)
async def mute(self, ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild

    for role in guild.roles:
        if role.name in ['muted', 'Muted']:
            await member.add_roles(role, reason=reason)
            await ctx.send(f'{member.mention} has been muted by {ctx.author.mention}')
            return

    overwrite = discord.PermissionOverwrite(send_messages=False)
    newRole = await guild.create_role(name='Muted')

    for channel in guild.text_channels:
        await channel.set_permissions(newRole, overwrite=overwrite)

    await member.add_roles(newRole)
    await ctx.send(f'{member.mention} has been muted by {ctx.author.mention}')


@bot.command()
@commands.has_guild_permissions(mute_members=True)
async def unmute(self, ctx, member: discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name in ['muted', 'Muted']:
            try:
                await member.remove_roles(role)
            except:
                await ctx.send('member is already unmuted')
                return

            await ctx.send(f'{member.mention} has been unmuted by {ctx.author.mention}')
            return

    await ctx.send('Muted role not found')
bot.run(token)  # important!
