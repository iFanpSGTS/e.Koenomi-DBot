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
		print('[+] Withdraw Code ACTIVE!')

	@commands.command()
	async def withdraw(self,ctx, amount = None):
	    await open_account(ctx.author)
	    if amount == None:
	        await ctx.send('Please enter amount')
	        return
	    balancee = await update_bank(ctx.author)

	    amount = int(amount)

	    if amount > balancee[1]:
	        await ctx.send('You poor retard')
	        return
	    if amount < 0:
	        await ctx.send('Please type corectly')
	        return
	    await update_bank(ctx.author,amount)
	    await update_bank(ctx.author,-1*amount, 'bank')
	    
	    await ctx.send(f'You withdraw {amount}wls from bank!')

async def update_bank(user,change = 0,mode = 'wallet'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open('./bank.json','w') as f:
        json.dump(users,f)

    balancee = [users[str(user.id)]['wallet'],users[str(user.id)]['bank']]
    return balancee

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