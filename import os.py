import os

import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

client = discord.Client()
default_intents = discord.Intents.default()
client = discord.Client(intents=default_intents)

default_intents.members = True



@client.event
async def on_ready():
    print("Le bot est prêt !")




@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith("!del5"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    if message.content == "Mohamed":
        await message.channel.send("Fanta")




@client.event
async def on_member_join(member):
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(959367147723829302)
    general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")




client.run(os.getenv("TOKEN"))