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
		print('[+] Shop Code ACTIVE!')

	@commands.command()
	async def shop(self,ctx):
	    embed = discord.Embed(title='Shop')
	    for item in ourshop:
	        name = item['name']
	        price = item['price']
	        embed.add_field(name=name, value=f'{price}wls')
	    await ctx.send(embed=embed)

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
           
def setup(bot):
	bot.add_cog(Economy(bot))