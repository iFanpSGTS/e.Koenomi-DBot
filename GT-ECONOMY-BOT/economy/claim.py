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
		print('[+] Claim Code ACTIVE!')

	@commands.command()
	async def claim(self,ctx):
	    user = ctx.author
	    users = await get_bank_data()
	    with open('trash_money.txt','r') as f:
	        money = f.read()
	        money = int(money)
	        if money == 0 or money < 0:
	            await ctx.send('No one trash their money!')
	        if money > 0:
	            await ctx.send('Congrats u got the trash money!')
	            f = open('trash_money.txt','r')
	            money = f.read()
	            money = int(money)
	            users[str(user.id)]['wallet'] += money
	            with open('./bank.json','w') as f:
	                json.dump(users,f)
	            f = open('trash_money.txt','w')
	            f.write('0')
	            f.close()

async def get_bank_data():
    with open('./bank.json','r') as f:
        users = json.load(f)
    return users
    
def setup(bot):
	bot.add_cog(Economy(bot))