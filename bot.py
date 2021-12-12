import os

from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(pass_context=True, name='hello', help='Hello World')
async def hello(ctx):
    await ctx.send('Hello World')

bot.run(TOKEN)
