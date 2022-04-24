import os
import discord
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")
client = discord.Client()
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for each_message in messages:
        await each_message.delete()
bot.run(os.getenv("TOKEN"))

