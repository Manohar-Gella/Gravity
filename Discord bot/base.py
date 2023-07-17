import discord
from discord.ext import commands

# Create a new bot instance
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready and connected to the server
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Say
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# Run the bot
bot.run('YOUR_BOT_TOKEN')
