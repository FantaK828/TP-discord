import os
import discord
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")
client = discord.Client()
from discord.ext import commands


class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
    async def on_ready(self):
        print("Le bot est prêt.")
    async def on_message(message):
        if message.content.startswith("!del5"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()
        if message.content == "Ping":
            await message.channel.send("Pong")
   
    async def on_member_join(member):
        print(f"L'utilisateur {member.display_name} a rejoint le serveur !")
        general_channel = client.get_channel(959367147723829302)
        general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")

bot = DocBot()
bot.run(os.getenv("TOKEN"))
