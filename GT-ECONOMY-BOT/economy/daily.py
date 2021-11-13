import discord
import subprocess
import os, random, re, requests, json
import asyncio
from datetime import datetime
from discord.ext import commands

class Economy(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('[+] Daily Code ACTIVE!')

	@commands.command()
	async def daily(self,ctx):
	    users = await get_bank_data()
	    user = ctx.author

	    daily_earn = random.randrange(600)
	    daily_earn = int(daily_earn)

	    if daily_earn > 0:
	    	await ctx.send(f'You recive {daily_earn}wls from daily earning!')
	    	users[str(user.id)]['wallet'] += daily_earn
	    	with open('./bank.json','w') as f:
	    		json.dump(users,f)
	    elif daily_earn == 0:
	    	await ctx.send(f'You didnt recive any wls from daily earning!')

async def get_bank_data():
	with open('./bank.json','r') as f:
		users = json.load(f)
	return users
	
async def open_account(user):
	users = await get_bank_data()

	with open('./bank.json','r') as f:
		users = json.load(f)
	if str(user.id) in users:
		return False
	else:
		users[str(user.id)] = {}
		users[str(user.id)]["wallet"] = 0
		users[str(user.id)]["bank"] = 0 
	with open('./bank.json','w') as f:
		json.dump(users,f)
	return True
   
def setup(bot):
	bot.add_cog(Economy(bot))