#joshua Isakson
#6/8/2021

import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix = '==') # creates the client(aka the bot) and assignes anything with '==' infornt of it as a command

@client.event      # on the event of on_ready(on startup) it will send the message that the bot is online
async def on_ready():   #creates a function that gets call on ready
    botspam = client.get_channel(851701508776525844) #tells the bot which channel to send the message to
    await botspam.send('The Damned is online.')  #the line that sends the message

@client.command(name = 'version') #assigns the command you need to put in for the but to know its this command so the command is ==version
async def version(message):   # creates a function that called whenever ==version gets typed into the botspam channel
    botspam = client.get_channel(851701508776525844)  
    embed = discord.Embed(title = 'The Damned', color = 0x00ff00)  #creates a discord embed titles 'The Damned' and assignes it a color
    embed.add_field(name = 'Verion:', value = 'v1.00')   #add a field to the embed
    embed.add_field(name = 'Releas date:', value = '6/8/2021 at 3:03am')
    embed.add_field(name = 'Author:',value = 'Made by Joshua Isakson')
    await botspam.send(embed = embed)  # send the embed to the bot spam channel

#testing command
@client.command(name = 'test') 
async def version(message):
    botspam = client.get_channel(851701508776525844)
    await botspam.send('test') 

@client.command(name = 'roll')
async def roll(message):
    botspam = client.get_channel(851701508776525844)
    content = message.content 
    spliced = content.split()
    spliced.remove('!')
    spliced.remove('d')
    embed = discord.Embed(title = "Your rolls are:",color = 0x00ff00)
    dicenum = int(spliced[0])
    diceval = int(spliced[1])
    total = 0
    while dicenum>0:
        randnum = random.randint(1,diceval)
        total = total+randnum
        embed.add_field(name = 'Roll:',value = randnum,inline = False)
        dicenum -= 1
    embed.add_field(name = 'Total Roll:',value = total,inline = False)
    await botspam.send(embed = embed)

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        botspam = client.get_channel(851701508776525844)
        content = message.content 
        spliced = content.split()
        spliced.remove('!')
        spliced.remove('d')
        embed = discord.Embed(title = "Your rolls are:",color = 0x00ff00)
        dicenum = int(spliced[0])
        diceval = int(spliced[1])
        total = 0
        while dicenum>0:
            randnum = random.randint(1,diceval)
            total = total+randnum
            embed.add_field(name = 'Roll:',value = randnum,inline = False)
            dicenum -= 1
        embed.add_field(name = 'Total Roll:',value = total,inline = False)
        await botspam.send(embed = embed)



client.run('ODUxNjg4NTY1NzIwNzQzOTQ2.YL76yQ.cUIf2KevBWKaR6wrKIjqtPra-iI')