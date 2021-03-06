import os

from discord.ext import commands
from discord import Intents

TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

print('Trying to start bot with token: %s' % TOKEN)


@bot.command(pass_context=True, name='hello', help='Hello World')
async def hello(ctx):
    await ctx.send('Hello World')

bot.run(TOKEN)
