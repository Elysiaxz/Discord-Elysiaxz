import os
import discord
from discord.ext import commands
from discord import app_commands
from Discordserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

#Start bot
@bot.event
async def on_ready():
    print("Bot online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

#Join the server/leave the server
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1144317271167221850) #ID Room
    text = f"Welcome to the server, {member.mention}!"

    emmbed = discord.Embed(title = "Welcome to the server!",
                          description = text,
                          color = 0x66FFFF)

    await channel.send(text) #Send message to room
    await channel.send(embed = emmbed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1144317271167221850)
    text = f"{member.mention} has left the server!"

    emmbed = discord.Embed(title = "has left the server!",
                           description = text,
                           color = 0x66FFFF)

    await channel.send(text)
    await channel.send(embed = emmbed)

#chatbot
@bot.event
async def on_message(message):
    mes = message.content
    if mes == "Hello":
        await message.channel.send("Hello It's me!")

    if mes == "hi Elysiaxz":
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message)

#Commands bot
@bot.tree.command(name='hellobot', description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message("Hello It's me BOT DISCORD")


@bot.tree.command(name='name')
@app_commands.describe(name = "What is you name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")


# Embeds

@bot.tree.command(name='help', description='Bot Commands')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='Help Me! - Bot Commands',
                           description='Bot Commands',
                           color=0x66FFFF,
                           timestamp= discord.utils.utcnow())

    # ใส่ข้อมูล
    emmbed.add_field(name='/help', value='for help', inline=True)
    emmbed.add_field(name='/hello', value='Hello Command', inline=True)
    emmbed.add_field(name='/play', value='play music', inline=False)

    # ใส่รูป small/big
    emmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1281568106753298453/1293842844926214174/59b46c28435ebd8a224c4368b2c503f2.jpg?ex=6708d88c&is=6707870c&hm=c0f424463896a92558562a4f7ffeab4e6187b637083de2814ecf1382c01b8d7e&")
    emmbed.set_image(url="https://img.freepik.com/free-vector/star-graphic-grunge-background_1409-8407.jpg?w=1380&t=st=1728547476~exp=1728548076~hmac=1e1ce90f822221a0902f362ce210f56b698133d8fb33b47556da812d357ebb0c")

    await interaction.response.send_message(embed = emmbed)

bot.run(os.getenv("TOKEN"))
