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
		print('[+] Beg Code ACTIVE!')

	@commands.cooldown(1, 180, commands.BucketType.user)
	@commands.command()
	async def beg(self,ctx):
	    await open_account(ctx.author)
	    user = ctx.author
	    users = await get_bank_data()

	    earning = random.randrange(4)

	    if earning == 0:
	        await ctx.send(f'Rip no one give you wls :(')

	    if earning > 0:
	        await ctx.send(f'Someone give you {earning}wls')

	    users[str(user.id)]["wallet"] += earning
	    with open('./bank.json','w') as f:
	        json.dump(users,f)

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

async def get_bank_data():
    with open('./bank.json','r') as f:
        users = json.load(f)
    return users
    
def setup(bot):
	bot.add_cog(Economy(bot))