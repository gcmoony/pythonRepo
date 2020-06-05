import discord
import os

# make sure to source it
# go to your bot folder
# type in "bot-env\Scripts\activate.bat"


client = discord.Client()


@client.event
async def on_ready():
    print('Yo yo, my nibba {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #if message.content.startswith('$poop'):
    #    await message.channel.send('I shitted')

    #if message.content.startswith('$dink'):
    #    await message.channel.send('https://youtu.be/ndAbIQD6Fs8')
    
    #if message.content.startswith('$oops'):
    #    await message.channel.send('big shit time ')

    if message.content.startswith('$maybe'):
        await message.channel.send('Chris is a black')

    if message.content.startswith('$test1'):
        await message.channel.send(file=discord.File('D:\\Pictures\\Stuff\\EthansRhino.png'))

    if message.content.startswith('$sleepTime'):
        await message.channel.send(file=discord.File('D:\\Pictures\\Stuff\\DONKEYTIMEOVER.png'))

    if message.content.startswith('$goHome'):
       await close()

    if message.content.startswith('$whoAmI'):
        print(message.author)



with open("textFilesLel\\keys.txt", "r") as file:
    key = file.readline()
client.run(key)