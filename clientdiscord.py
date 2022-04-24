import os
import discord
from dotenv import load_dotenv
from discord import Client
load_dotenv(dotenv_path="config")

client = discord.Client()
class MyBot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

client.run(os.getenv("TOKEN"))