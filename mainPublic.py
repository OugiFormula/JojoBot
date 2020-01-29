import discord
from discord.ext import commands
import asyncio
import time
import typing
import os

Client = discord.Client
client = commands.Bot(command_prefix = "jojo!")

@client.event
async def on_ready():
  print ("------------------------------------")
  print ("Bot Name: " + client.user.name)
  print ("Discord Version: " + discord.__version__)
  print ("------------------------------------")
  await client.change_presence(activity=discord.Game(name='With Jotaro'))


@client.event
async def on_message(message):
  channel = message.channel
  everyone = message.guild.default_role
  if message.content.startswith('STAR PLATINUM!'):
      with open('ora.gif', 'rb') as picture:
          await channel.send(file=discord.File(picture, 'ora.gif'))

  if message.content.startswith('ZA WARUDO!'):
    with open('zawarudo.gif', 'rb') as picture:
      await channel.send(file=discord.File(picture,'zawarudo.gif'))
      await channel.set_permissions(everyone, send_messages=False)
      await asyncio.sleep(10)
      await channel.set_permissions(everyone, send_messages=True)

  if message.content.startswith('STAR PLATINUM ZA WARUDO!'):
    with open('spzawarudo.gif', 'rb') as picture:
      await channel.send(file=discord.File(picture,'spzawarudo.gif'))
      await channel.set_permissions(everyone, send_messages=False)


  if message.content.startswith('time has begun to move again'):
    with open('timebegin.gif', 'rb') as picture:
      await channel.send(file=discord.File(picture,'timebegin.gif'))
      await channel.set_permissions(everyone, send_messages=True)


client.run('TOKEN HERE')
