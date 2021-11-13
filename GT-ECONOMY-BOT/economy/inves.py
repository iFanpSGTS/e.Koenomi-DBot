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
        print('[+] Inves Code ACTIVE!')

    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.command()
    async def inves(self,ctx,amounts):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        wls = users[str(user.id)]["wallet"]

        if wls < 100 or wls == 100:
            await ctx.send('You cant inves under 100wls')

        timess3 = 86400

        if wls > 100:
            amounts = int(amounts)
            total_inves = random.randrange(10000000)
            if total_inves < amounts or total_inves == amounts:
                await ctx.send("You succesfully join the Hydra invesment\nWait for 1day to get profit!")
                users[str(user.id)]["wallet"] -= int(amounts)
                with open('./bank.json','w') as f:
                    json.dump(users,f)
                while True:
                    timess3 -= 1
                    if timess3 == 0:
                        await ctx.send("Sorry, you're not profit, join again later.")
                    # print(f'[{user.name}] Investation time = {timess3}')
                    await asyncio.sleep(1)
            if total_inves > amounts:
                await ctx.send("You succesfully join the Hydra invesment\nWait for 1day to get profit!")
                users[str(user.id)]["wallet"] -= int(amounts)
                with open('./bank.json','w') as f:
                    json.dump(users,f)
                while True:
                    timess3 -= 1
                    if timess3 == 0:
                        await ctx.send('You got profit from investation!')
                        users[str(user.id)]["bank"] += total_inves
                        with open('./bank.json','w') as f:
                            json.dump(users,f)
                    # print(f'[{user.name}] Investation time = {timess3}')
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
    
def setup(bot):
    bot.add_cog(Economy(bot))