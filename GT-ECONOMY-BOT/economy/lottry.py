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
		print('[+] Lottry Code ACTIVE!')

	@commands.command()
	async def lottry(self,ctx,money):
	    await open_account(ctx.author)
	    user = ctx.author
	    users = await get_bank_data()
	    money = int(money)
	    if users[str(user.id)]['wallet'] == 0:
	        await ctx.send('You cant lottry without money!')
	        return 

	    result = []
	    for slot in range(3):
	        a = random.choice(["X","D","A"])
	        result.append(a)

	    await ctx.send(f'{str(result)}')

	    if result[0] == result[1] or result[0] == result[2] or result[2] == result[1]:
	        await ctx.send('You won the lottry!')
	        users[str(user.id)]['wallet'] -= int(money)
	        with open('./bank.json','w') as f:
	            json.dump(users,f)
	        if money < 100 or money == 100:
	            users[str(user.id)]['wallet'] += 8*money
	            with open('./bank.json','w') as f:
	                json.dump(users,f)
	        elif money > 100:
	            users[str(user.id)]['wallet'] += 3*money
	            with open('./bank.json','w') as f:
	                json.dump(users,f)
	    else:
	        users[str(user.id)]['wallet'] -= int(money)
	        with open('./bank.json','w') as f:
	            json.dump(users,f)
	        await ctx.send('Sorry you dont win anything!')

async def open_account(user):
    users = await get_bank_data()

    with open('././bank.json','r') as f:
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
    with open('././bank.json','r') as f:
        users = json.load(f)
    return users
    
def setup(bot):
	bot.add_cog(Economy(bot))