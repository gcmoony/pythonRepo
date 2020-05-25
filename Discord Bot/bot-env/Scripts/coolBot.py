import discord
import asyncio
import datetime
import codecs
import mapPicker
import random
import youtube_dl
from discord.ext import commands

# created a bot variable as 'client'
client = commands.Bot(command_prefix = '>')
players = {}

# This just shows when the bot is initialized to run
@client.event
async def on_ready():
    print("I'm Ready")


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')


@client.command()
@commands.has_role('Stickiest Poop Sock')
async def clear(ctx, amount = 50):
    await ctx.channel.purge(limit = amount + 1)



# Voice Channel Commands
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    


@client.command()
async def leave(ctx):
    #for clientChannel in client.voice_clients:
    #    await clientChannel.disconnect()
    voiceClient = client.voice_clients.pop()
    await voiceClient.disconnect()



#@client.event
#async def on_typing(channel, member, datetime):
#    await channel.send(f'{str(member)[:-5]} is typing, what they gonna say tho?')


# Music testing
@client.command(pass_context = True)
async def play(ctx, url):
    await join(ctx)
    server = ctx.guild
    #print(help(ctx))
    #print(ctx.guild)
    voiceClient = client.voice_clients.pop()
    musicPlayer = youtube_dl.YoutubeDL()
    await musicPlayer.download(url)
    #print(server)


# Other commands
@client.command()
async def ttsTime(ctx, *args):
    loc = ctx.message.channel
    phrase = ""
    for content in args:
        phrase = phrase + content + " "
    await ctx.channel.purge(limit = 1)
    await loc.send(phrase, tts=True)


@client.command()
async def flip(ctx):
    choice = random.choice(["Heads", "Tails"])
    await ctx.send(choice)


@client.command()
async def pickTarkov(ctx):
    await ctx.send(mapPicker.chooseMap())


@client.command()
@commands.has_role('Stickiest Poop Sock')
async def hey(ctx):
    await ctx.send('oh god oh fuck')

@client.command()
async def youcuck(ctx):
    with codecs.open("bot-env\\Scripts\\textFilesLel\\reverseAscii.txt", "r", "utf-8") as file:
        returnString = file.read()
    await ctx.send(f'{returnString}')


@client.command(aliases=['wow', 'doge'])
async def _wow(ctx):
    with codecs.open("bot-env\\Scripts\\textFilesLel\\dogeTime.txt", "r", "utf-8") as file:
        returnString = file.read()
    await ctx.send(f'{returnString}')


@client.command()
async def hmm(ctx):
    with codecs.open("bot-env\\Scripts\\textFilesLel\\hmm.txt", "r", "utf-8") as file:
        returnString = file.read()
    await ctx.send(f'{returnString}')


## Testing Some stuff ##
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #if str(message.author) == "PoopSock#7407":
    #    await message.channel.send("PoopSock said something cool!")

    #if str(message.author) == "QuantumCreamPi#8117":
    #    await message.channel.send("Shut up, you're literally black")
    #await message.channel.send(f'{str(message.author)[:-5]} said something!')

    if (str(message.author) == "PoopSock#7407" and message.content.startswith('$badBot')):
        await message.channel.send("I don't feel so good...")
        client.close()

    if (str(message.author) == "PoopSock#7407" and message.content.startswith('$cum')):
        await message.channel.send("I just fucking nutted")

    if (message.content.startswith('$cum') and str(message.author) != "PoopSock#7407"):
        await message.channel.send("That's big gay")

    if (message.content.startswith('$badBot') and str(message.author) != "PoopSock#7407"):
        await message.channel.send(f"You don't own me {str(message.author)}")

    await client.process_commands(message)


# Allows code to connect with the application
client.run('NjgzNTcyMjUwMjQyNTgwNTI5.XlthOQ.fxoXuba1ysp6Un-EFkbppXjc6z0')

