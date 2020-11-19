import discord
from discord.ext import commands, tasks
import random # Without this our 8ball would not work
import os

client = commands.Bot(command_prefix="=")

client.remove_command("help") # removes default help command! you can remove every command with this!

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Help')
    embed.add_field(name='Ping Command (=ping)', value='Returns the bots Latency!', inline=False)
    embed.add_field(name='Ban Command(=ban <user> <reason>)', value='Will ban the user that is mentioned', inline=False)
    embed.add_field(name='Kick Command(=kick <user> <reason>)', value='Will kick the user that is mentioned', inline=False)
    embed.add_field(name='8ball Command(=8ball <message>)', value='Will pick a random responce', inline=False)
    embed.add_field(name='unban Command(=unban <user>)', value='Will unban the user that is mentioned', inline=False)
    embed.add_field(name='clear Command(=clear <amount>)', value='Will clear the amount mentioned', inline=False)
    await ctx.send(author, embed=embed)


@client.event # Is something that always runs
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Listening for =help')) # Changes status
    print("Bot is Online")



@client.event
async def on_member_join(member): # Tells you when a member joins
    print(f'{member} has Hopped into the server')


@client.event
async def on_member_remove(member): # Tell's you when a member has left
    print(f'{member} has left the server sadly')


@client.command() # A command is something that you can run
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms') # It has to have round or it will be in decimal

@client.command(aliases=['8ball', 'eightball']) # eightball command
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt!",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."
                "Hmmmmmmmmmm.",
                "Caculating",
                "No clue."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command() # Amount is the default amount
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount) # You would do -clear amount


@client.command() # kick cmd
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)



@client.command() # ban cmd
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@commands.command() # Unban cmd
@commands.has_permissions(ban_members=True)
async def unban(self, ctx, member: discord.User):
        await ctx.guild.unban(member)
        await ctx.send(f'Unbanned {member.name}')




client.run('Token goes herel.')
