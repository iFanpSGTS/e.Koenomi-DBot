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
		print('[+] Addmoney Code ACTIVE!')

	@commands.command()
	@commands.is_owner()
	async def addmoney(self,ctx,member: discord.Member,amount):
	    await open_account(ctx.author)
	    await open_account(member)
	    user = ctx.author
	    users = await get_bank_data()
	    amount = int(amount)
	    balancee = await update_bank(ctx.author)

	    await update_bank(member,amount, 'bank')

	    await ctx.send(f'Succes sending money to {member.mention}')

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

async def update_bank(user,change = 0,mode = 'wallet'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open('./bank.json','w') as f:
        json.dump(users,f)

    balancee = [users[str(user.id)]['wallet'],users[str(user.id)]['bank']]
    return balancee

def setup(bot):
	bot.add_cog(Economy(bot))