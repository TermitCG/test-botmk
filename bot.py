import discord

client = discord.Client()

@client.event
async def on_message(message)
    message.concent.lower()
    if message.author == client.user:
        return
    if message.concent == ("test"):
        await message.channel.send("Testowanic")

client.run('BOT TOKEN')

