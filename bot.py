import os
import json
import discord
import random
import re
import requests 

from dotenv import load_dotenv
from riddles import get_riddle
from urllib.parse import urlparse


# functionality

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')

bot = discord.Client()

@bot.event
async def on_ready():
	# limit commands to run only in the groepkakken server
	for guild in bot.guilds:
		if guild.name == GUILD:
			break

	print(f'{bot.user} has successfully connected to {guild.name}\n')

	await bot.change_presence(activity=discord.Game(name='the game of life.'))
	members = '\n - '.join([f'{member.name} : {member.id}'for member in guild.members])
	print(f'Guild Members:\n - {members}')
	
	print('\nChannels in this server:')
	for channel in guild.text_channels:
		print(f' - {channel} : {channel.id}')
	print('\n')

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return #ignore our own commands

	if message.content.startswith('!'):
		args = message.content.split(" ")
		cmd  = args[0].strip("!")
		if cmd == "flip":
			coin = "heads" if random.randint(1,10) > 5 else "tails"
			await message.channel.send("The coin shows: " + coin + ".")
		elif cmd == "hello":
			await message.channel.send("hello!")
		elif cmd == "pick":
			if len(args) == 1:
				await message.channel.send("Incorrect use of !pick command. Please use as follows, seperating each choice with a comma (,):\n" + "```!pick choice1, choice2, choice3, ..., choice999```")                
			else:
				choices = re.split("\,\s?", message.content[6:]) # works both with and without a space
				choice = random.choice(choices)
				await message.channel.send("The oracle has chosen! The choice is:\n" + choice)
		elif cmd == "roll":
			default_dice = 6
			if len(args) == 2:
				default_dice = int(args[1])
			
			dice = random.randint(1, default_dice)
			await message.channel.send("The dice lands on: " + str(dice) + ".")
		elif cmd == "riddle":
			riddle_array = get_riddle()
			riddle = riddle_array[0]
			await message.channel.send(f'{riddle_array[0]}\n||{riddle_array[1]}||')
		

bot.run(TOKEN)








