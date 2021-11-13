import discord
import subprocess
import os, random, re, requests, json
import asyncio
from datetime import datetime
from discord.ext import commands

class Information(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('[+] Reroll Code ACTIVE!')

	@commands.command()
	async def reroll(self,ctx, id_: int):
	    try:
	        new_msg = await ctx.channel.fetch_message(id_)
	    except:
	        await ctx.send('Giveaway message id is error!')
	        return

	    users = await new_msg.reactions[0].users().flatten()
	    users.pop(users.index(ctx.guild.me))

	    winner = random.choice(users)

	    await ctx.send(f'New winner is {winner}')

def setup(bot):
	bot.add_cog(Information(bot))