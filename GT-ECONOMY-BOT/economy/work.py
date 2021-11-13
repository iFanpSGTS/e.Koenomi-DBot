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
		print('[+] Work Code ACTIVE!')

	@commands.cooldown(1, 86400, commands.BucketType.user)
	@commands.command()
	async def work(self,ctx):
		work = ['Taxi',
				'Jester',
				'Scammer',
				'Stripteas',
				'BodyGuard',
				'Business']
		await open_account(ctx.author)
		user = ctx.author
		users = await get_bank_data()
		work_ch = random.choice(work)

		if work_ch == 'Taxi':
			await ctx.send("You be a Taxi Driver! you got 100wls from working on Taxi!")
			users[str(user.id)]["bank"] += 100
			with open('./bank.json','w') as f:
				json.dump(users,f)
		if work_ch == 'Jester':
			await ctx.send("You be a Jester! you got 50wls from working on Jester!")
			users[str(user.id)]["bank"] += 50
			with open('./bank.json','w') as f:
				json.dump(users,f)
		elif work_ch == 'Scammer':
			money_sc = random.randrange(1000)
			money_sc = int(money_sc)
			await ctx.send(f"You be a Scammer! you got {money_sc}wls from working on Scammer!")
			users[str(user.id)]["bank"] += money_sc
			with open('./bank.json','w') as f:
				json.dump(users,f)
		elif work_ch == 'Stripteas':
			await ctx.send("You be a Stripteas Girl! you got 500wls from working on Stripteas!")
			users[str(user.id)]["bank"] += 500
			with open('./bank.json','w') as f:
				json.dump(users,f)
		elif work_ch == 'BodyGuard':
			await ctx.send("You be a BodyGuard! you got 200wls from working on Hydra!")
			users[str(user.id)]["bank"] += 200
			with open('./bank.json','w') as f:
				json.dump(users,f)
		elif work_ch == 'Business':
			await ctx.send("You be a Business Man! you got 1000wls from working on Food Delivery!")
			users[str(user.id)]["bank"] += 1000
			with open('./bank.json','w') as f:
				json.dump(users,f)

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