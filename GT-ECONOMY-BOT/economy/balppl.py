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
		print('[+] Bal Code ACTIVE!')

	@commands.command()
	async def balppl(self, ctx, orang:discord.Member):
		await open_account(orang)
		user = orang
		users = await get_bank_data()

		wallet = users[str(user.id)]["wallet"]
		bank   = users[str(user.id)]["bank"] 
		embed = discord.Embed(title=f"{user.name} Balance")
		embed.add_field(name='Wallet:\n', value=f'{wallet}wls')
		embed.add_field(name='Safe:\n', value=f'{bank}wls saved')
		if wallet > 100000:
			await ctx.send('Your money is too much in your wallet please try to deposit!')
		if wallet < 100000 or wallet == 100000:
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
    with open('./bank.json','w') as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open('./bank.json','r') as f:
        users = json.load(f)
    return users

def setup(bot):
	bot.add_cog(Economy(bot))