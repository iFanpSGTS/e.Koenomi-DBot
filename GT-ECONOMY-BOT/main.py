import discord
import os
import glob, os
import os, json
from discord.ext import commands

prefix = '!!'

bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('[+]======ALL FILES WORKED!======[+]\n')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Thats command is unreachable or the owner didnt make that command!')
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.command.qualified_name == 'giveaway':
            await ctx.send('Please put time and prize\n10s/m/h/d and prize')
        if ctx.command.qualified_name == 'addmoney':
            await ctx.send('!!addmoney [user] [wls]')
        if ctx.command.qualified_name == 'transfer' or ctx.command.qualified_name == 'tf':
            await ctx.send('!!tf|transfer [user] [wls]')
        if ctx.command.qualified_name == 'reroll':
            await ctx.send('!!reroll [giveaway msg id]')
        if ctx.command.qualified_name == 'inves':
            await ctx.send('!!inves [amount wls]')
        if ctx.command.qualified_name == 'withdraw' or ctx.command.qualified_name == 'deposit':
            await ctx.send('Put the wls amount')
        if ctx.command.qualified_name == 'buy' or ctx.command.qualified_name == 'sell':
            await ctx.send('Put [item-name] [amount]')
        if ctx.command.qualified_name == 'gacha':
            await ctx.send('!!gacha [Box-gacha] [amount]')
        if ctx.command.qualified_name == 'lottry':
            await ctx.send('!!lottry [spent money]\nif you spent under 100wls your money will x8 but if you spent more than 100wls your money will x3')
        if ctx.command.qualified_name == 'balppl':
            await ctx.send('!!lottry [@person]')
    if isinstance(error, commands.CommandOnCooldown):
        if ctx.command.qualified_name == 'work':
            await ctx.send('You can work again 1d from now!')
        elif ctx.command.qualified_name == 'beg':
            await ctx.send('You can only beg every 2min from now!')
        elif ctx.command.qualified_name == 'inves':
            await ctx.send('You can only make invesment 1d/1 inves!')
        elif ctx.command.qualified_name == 'trashmoney':
            await ctx.send('Wait 1minute to trash ur money!')
        await ctx.send('Command had cooldown time!')
    if isinstance(error, commands.MissingRole):
        await ctx.send('You dont have access to use the command!')
    print(error)

@commands.is_owner()
@bot.command()
async def load_eco(ctx, extension):
    bot.load_extension(f'economy.{extension}')

@commands.is_owner()
@bot.command()
async def unload_eco(ctx, extension):
    bot.unload_extension(f'economy.{extension}')

@commands.is_owner()
@bot.command()
async def load_info(ctx, extension):
    bot.load_extension(f'information.{extension}')

@commands.is_owner()
@bot.command()
async def unload_info(ctx, extension):
    bot.unload_extension(f'information.{extension}')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='[+]==Help Center==[+]', description=f'[+]{prefix}help_economy[+]\n(Show all economy command)\n[+]{prefix}help_info[+]\n(Show all info command)')
    embed.set_footer(text='Bot by iFanpS, (c) 2021')
    await ctx.send(embed=embed)

@bot.command()
async def help_economy(ctx):
    embed = discord.Embed(title='[+]========Economy========[+]')
    os.chdir("./economy")
    for file in glob.glob("*.py"):
        file1 = file.replace('.py', ' ')
        embed.add_field(name=file1.upper(), value='worked!')
    await ctx.send(embed=embed)

@bot.command()
async def help_info(ctx):
    embed = discord.Embed(title='[+]========Information========[+]')
    os.chdir("./information")
    for file in glob.glob("*.py"):
        file1 = file.replace('.py', ' ')
        embed.add_field(name=file1.upper(), value='worked!')
    await ctx.send(embed=embed)

for file in os.listdir('./economy'):
    if file.endswith('.py'):
        bot.load_extension(f'economy.{file[:-3]}')

for file in os.listdir('./information'):
    if file.endswith('.py'):
        bot.load_extension(f'information.{file[:-3]}')

@bot.command(aliases=['lb'])
async def leaderboard(ctx,x=5):
    users = await get_bank_data()
    leader_board = {}
    total = []

    for user in users:
        name = int(user)
        total_amtt = users[user]['wallet'] + users[user]['bank']
        leader_board[total_amtt] = name 
        total.append(total_amtt)

    total = sorted(total,reverse=True)

    embed = discord.Embed(title=f'Top {x} Leaderboard', description='Top Rich People')
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = await bot.fetch_user(id_)
        embed.add_field(name=f'{index}. {member}', value=f'{amt}wls', inline=False)
        if index == x:
            break
        else:
            index +=1
    await ctx.send(embed=embed)

async def get_bank_data():
    with open('bank.json','r') as f:
        users = json.load(f)
    return users

bot.run('OTA4MjU4NzgxMzA0MDc0Mjcx.YYzH6A.Eb_41lxyIgzmPQWonXUxpe9MPGw')
