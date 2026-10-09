from email import message

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$demir':
        await message.channel.send(file=discord.File('images/demir.jpg'))

    elif message.content == '$kağıt':
        await message.channel.send(file=discord.File('images/kağıt.jpg'))

    elif message.content == '$cam':
        await message.channel.send(file=discord.File('images/cam.jpg'))

    elif message.content == '$plastik':
        await message.channel.send(file=discord.File('images/plastik.jpg'))

    elif message.content == '$radyasyon':
        await message.channel.send(file=discord.File('images/radioactivity.jpg'))

    elif message.content == '$hastane':
        await message.channel.send(file=discord.File('images/hastane.jpg'))

    elif message.content == '$organik':
        await message.channel.send(file=discord.File('images/organik.jpg'))


client.run("MTU1MDE1NTI2ODQzMDQ5OTkzMQ.GMjFHy.ixEFd1A6ts4L6MOPZTqHl78xOey0qugkNi2ZtA")

