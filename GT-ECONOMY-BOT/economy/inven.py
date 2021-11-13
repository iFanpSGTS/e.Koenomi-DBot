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
		print('[+] Inven Code ACTIVE!')

	@commands.command()
	async def inven(self, ctx):
	    await open_account(ctx.author)
	    user = ctx.author
	    users = await get_bank_data()

	    try:
	        bag = users[str(user.id)]['bag']
	    except:
	        bag = []

	    embed = discord.Embed(title='Inventory')
	    for item in bag:
	        name = item['item']
	        amount = item['amount']
	        embed.add_field(name=name, value=f'{amount} Items')
	    await ctx.send(embed=embed)

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
    with open('bank.json','w') as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open('./bank.json','r') as f:
        users = json.load(f)
    return users

def setup(bot):
	bot.add_cog(Economy(bot))