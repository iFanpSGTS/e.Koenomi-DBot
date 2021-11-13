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
		print('[+] Gacha Code ACTIVE!')

	@commands.command()
	async def gacha(self, ctx,item,amount=1):
	    if item == 'poke-card' or item == 'box-gacha':
	        await open_account(ctx.author)
	        res = await gacha_this(ctx.author,item,amount)
	        user = ctx.author
	        users = await get_bank_data()
	        hasil_bg = random.randrange(250)
	        hasil_cp = random.randrange(450)

	        if not res[0]:
	            if res[1] == 1:
	                await ctx.send('Cannot specified object!')
	            if res[1] == 2:
	                await ctx.send('You dont have gacha items!')
	            if res[1] == 3:
	                await ctx.send(f'You dont have {item} to gacha')
	        if res[0]:
	            if item == 'box-gacha':
	                if hasil_bg > 100:
	                    await ctx.send(f'Congrats! you win the gacha!')
	                    users[str(user.id)]["wallet"] += hasil_bg*amount
	                    with open('./bank.json','w') as f:
	                        json.dump(users,f)
	                elif hasil_bg < 100:
	                    await ctx.send(f'You dont win anything!')
	                elif hasil_bg == 100:
	                    await ctx.send('You didnt lose or win. you just got nothing!')
	            elif item == 'poke-card':
	                if hasil_cp > 250:
	                    await ctx.send(f'Congrats! you win the gacha!')
	                    users[str(user.id)]["wallet"] += hasil_cp*amount
	                    with open('./bank.json','w') as f:
	                        json.dump(users,f)
	                elif hasil_cp < 250:
	                    await ctx.send(f'You dont win anything!')
	                elif hasil_cp == 250:
	                    await ctx.send('You didnt lose or win. you just got nothing!')

ourshop = [{"name":"diamond-axe","price":400},
           {"name":"rift-cape","price":650},  
           {"name":"lava-cape","price":500},
           {"name":"diamond-shoes","price":50},
           {"name":"fishnet","price":2},
           {"name":"da-vinci","price":990},
           {"name":"l-bot","price":1000},
           {"name":"gab","price":800},
           {"name":"golden-diaper","price":800},
           {"name":"box-gacha","price":100},
           {"name":"poke-card","price":250}]

async def gacha_this(user,item_name,amount,price=None):
    item_name = item_name
    name_ = None
    for item in ourshop:
        name = item['name']
        if name == item_name:
            name_ = name
            if price ==None:
                price = item['price']
            break

    if name_ == None:
        return [False,1]

    cost = price*amount
    users = await get_bank_data()
    balancee = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]['bag']:
            n = thing['item']
            if n == item_name:
                old_amt = thing['amount']
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]['bag'][index]['amount'] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False,3]
    except:
        return [False,3]
    
    with open('./bank.json','w') as f:
        json.dump(users,f)
    
    await update_bank(user,cost,'wallet')

    return [True,'Worked']

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