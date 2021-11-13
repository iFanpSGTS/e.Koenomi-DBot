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
        print('[+] Leaderboard Code ACTIVE!')

    @commands.command()
    async def leaderwdadwaboard(self,ctx):
        pass ## gw taruh file ini cuma buat on_ready nya

async def get_bank_data():
    with open('./bank.json','r') as f:
        users = json.load(f)
    return users

def setup(bot):
    bot.add_cog(Economy(bot))