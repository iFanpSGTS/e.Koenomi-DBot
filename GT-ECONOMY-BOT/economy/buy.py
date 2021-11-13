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
		print('[+] Buy Code ACTIVE!')

	@commands.command()
	async def buy(self,ctx,item,amount = 1):
	    await open_account(ctx.author)

	    res = await buy_this(ctx.author,item,amount)

	    if not res[0]:
	        if res[1] == 1:
	            await ctx.send('The item is outofstock')
	        if res[1] == 2:
	            await ctx.send(f'You poor man go away')
	    if res[0]:
	        await ctx.send(f'You just bought {amount} {item}')

ourshop = [{}] ##Taruh nama nama barang yang ingin di jual // contoh ada di file shop.py

async def update_bank(user,change = 0,mode = 'wallet'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open('./bank.json','w') as f:
        json.dump(users,f)

    balancee = [users[str(user.id)]['wallet'],users[str(user.id)]['bank']]
    return balancee

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in ourshop:
        name = item['name'].lower()
        if name == item_name:
            name_ = name
            price = item['price']
            break

    if name_ == None:
        return [False,1]

    cost = price*amount
    users = await get_bank_data()
    balancee = await update_bank(user)

    if balancee[0]<cost:
        return [False,2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]['bag']:
            n = thing['item']
            if n == item_name:
                old_amt = thing['amount']
                new_amt = old_amt + amount
                users[str(user.id)]['bag'][index]['amount'] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item":item_name, "amount" : amount}
            a = users[str(user.id)]['bag']
            a.append(obj)
    except:
        obj = {"item":item_name, "amount" : amount}
        users[str(user.id)]['bag'] = [obj]
    
    with open('./bank.json','w') as f:
        json.dump(users,f)
    
    await update_bank(user,cost*-1,'wallet')

    return [True,3]

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