WELCOME_MESSAGE = """
██████╗░░█████╗░░██╗░░░░░░░██╗███████╗██████╗░██████╗░░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║░░░░░  ╚════██╗██╔══██╗╚════██╗╚════██╗
██████╔╝██║░░██║░╚██╗████╗██╔╝█████╗░░██████╔╝██████╦╝███████║██║░░░░░██║░░░░░  ░░███╔═╝██║░░██║░░███╔═╝░░███╔═╝
██╔═══╝░██║░░██║░░████╔═████║░██╔══╝░░██╔══██╗██╔══██╗██╔══██║██║░░░░░██║░░░░░  ██╔══╝░░██║░░██║██╔══╝░░██╔══╝░░
██║░░░░░╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║██████╦╝██║░░██║███████╗███████╗  ███████╗╚█████╔╝███████╗███████╗
╚═╝░░░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝  ╚══════╝░╚════╝░╚══════╝╚══════╝"""
print(WELCOME_MESSAGE)

import num_generator
import discord
from discord.ext import commands

TOKEN = "MTAzMzI1MTc3Mzk4MjQ1Nzg3Nw.G-9hDn.jKDAfjkW8kWDRWKfWVYfWvl8Svild37yl_huxY"

# num_of_tickets = int(input("How many tickets you want: "))
#

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='=', intents=intents)


@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):

  #Checks for bot
  if message.author == bot.user:
    return
  # listen for commands
  if message.author.id == 543156600278614031:
    await message.channel.send("You are banned")
    return
  await bot.process_commands(message)


@bot.command()
async def generate(ctx, num):
  num_of_tickets = int(num)
  for _ in range(0, num_of_tickets, 1):
    ticket = num_generator.num_generate()
    await ctx.send(ticket)


bot.run(TOKEN)
