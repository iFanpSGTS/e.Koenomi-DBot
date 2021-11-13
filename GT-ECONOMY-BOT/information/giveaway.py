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
		print('[+] Giveaway Code ACTIVE!')

	@commands.command()
	async def giveaway(self,ctx, timess, *, prize):
	    timess2 = int(timess)
	    embed = discord.Embed(title = 'Giveaway!!!', description=prize)
	    embed.set_footer(text=f'Host: {ctx.author}')
	    message = await ctx.send(f'Giveaway Times end at: {timess}s')
	    em = await ctx.send(embed=embed)
	    await em.add_reaction('🎉')

	    while True:
	        timess2 -= 1
	        if timess2 == 0:
	            await message.edit(content='Giveaway has ended!')
	            break
	        await message.edit(content=f'Giveaway Times end at: {timess2}s')
	        await asyncio.sleep(1)

	    messages = await ctx.channel.fetch_message(em.id)
	    users = await messages.reactions[0].users().flatten()
	    users.pop(users.index(ctx.guild.me))

	    if len(users) == 0:
	        await ctx.send('No one join, no one win!')
	    
	    winner = random.choice(users)
	    prize1 = prize.upper()

	    await ctx.send(f'Congrats {winner.mention} has winning {prize1}')
	    
def setup(bot):
	bot.add_cog(Information(bot))