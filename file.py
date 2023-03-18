import discord 
from discord.ext import commands
from pathlib import Path
import pdf2docx

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def convert(ctx, attachment: discord.Attachment):
    file_name = attachment.filename
    file_data = await attachment.read()
    with open(file_name, "wb") as f:
        f.write(file_data)
    docx_file_name = pdf2docx.convert_pdf_to_docx(file_name)
    docx_file_name = Path(docx_file_name)
    with open(docx_file_name, "rb") as f:
        file_data = f.read()
    await ctx.channel.send(file=discord.File(docx_file_name, filename="converted.docx"),
                           content="Here is your converted file!")

bot.run("MTAzMzI1MTc3Mzk4MjQ1Nzg3Nw.GsTufY.IPrkkCw_Uie0tVXXaDs9gAVeGIJ6pVh3iEMrMM")