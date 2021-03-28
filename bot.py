import discord
from discord.ext import commands
from discord import file
import os
import requests
import json
import csv

description = '''A bot to get all members of discord'''

TOKEN = os.getenv('TOKEN')
CHANNEL = os.getenv('CHANNEL')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='users', brief='Get list of all users')
async def users(ctx):
    if (ctx.channel.name == CHANNEL):
        # ?users: Gathers the names of all users on the server and prints them to a CSV$
        await ctx.send("Getting user list...")
        users = []
        for member in ctx.message.guild.members:
            users.append(member.name)
        print(users)
        file_name = 'users.csv'

        with open('users.csv', 'w') as output:
            writer = csv.writer(output)
            writer.writerow(['Name'])
            for user in users:
                writer.writerow([user])

        with open('users.csv', 'rb') as export:
            await ctx.send(file=discord.File(export, 'users.csv'))

        with open('users.csv','w'): pass

bot.run(TOKEN)
