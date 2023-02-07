import os
import discord
import MarkovChain

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.content)
    if message.content.startswith('$hello'):
        msg = "Hi there!"
        #msg = MarkovChain.make_text(MarkovChain.chains, 4)
        #print(msg)
        await message.channel.send(msg)

        

client.run(os.environ['DISCORD_TOKEN'])