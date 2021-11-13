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
		print('[+] Trashmoney Code ACTIVE!')

	@commands.cooldown(1, 60, commands.BucketType.user)
	@commands.command(aliases=['tm'])
	async def trashmoney(self,ctx,amount:int):
	    await open_account(ctx.author)
	    user = ctx.author
	    users = await get_bank_data()
	    balancee = await update_bank(ctx.author) 

	    time = 10
	    if amount > balancee[0]:
	        await ctx.send('You poor lmao! what money u want to TRASH! NOOB!!!')
	        return
	    if amount < 0:
	        await ctx.send('You are poor or wrong put amount?')
	        return
	    await update_bank(ctx.author,-1*amount, 'wallet')
	    await ctx.send(f"{user} Trash he money! type [!!claim] to get the money!")
	    msg = await ctx.send(f'Member had {time}s to claim!')
	    with open('trash_money.txt','w') as f:
	        f.write(str(amount))
	        f.close()

	    while True:
	        time -= 1
	        if time == 0:
	            f = open('trash_money.txt','r')
	            if f.read() == '0':
	                await ctx.send('Someone claimed the trash money!')
	            else:
	                await ctx.send('No one claimed the trash money!')
	            break
	        await msg.edit(content=f'Member had {time}s to claim!')
	        await asyncio.sleep(1)

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