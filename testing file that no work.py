#Joshua Isakson
#6/5/2021
import random  
import discord





client = discord.Client()



@client.event
async def on_ready():
    botspam = client.get_channel(851701508776525844)
    await botspam.send('The Damned is online.')

@client.event
async def on_message(message):
    if message.content('==help'):
        botspam = client.get_channel(851701508776525844)
        
        await botspam.send('test')

botspam = client.get_channel(851701508776525844)

#helpembed = discord.Embed(title = 'Command List:',color = 0xFF0000)
#helpembed.add_field(title = "Dice Rolling:",value = '! followed by "number of dice" d "value of dice".')
#helpembed.add_field(title = 'version',value = 'The version command displays the latest version of the bot, its inital creation date and time, and who its creator is.')
#helpembed.add_field(title = 'yes')
#await botspam.send('word')
#await botspam.send(embed = helpembed)
    


#botspam = client.get_channel(851701508776525844)
#versionembed = discord.Embed(title = 'Version')
#versionembed.add_field(title = 'Version: v1.00')
#versionembed.add_field(title = 'Inital release: 6/8/2021')
#versionembed.add_field(title = 'Created by Joshua Isakson')

#await botspam.send(embed = versionembed)


@client.event
async def on_message(message):
    if message.content.startswith('@'):
        botspam = client.get_channel(851701508776525844)
        content = message.content 
        spliced = content.split()
        spliced.remove('!')
        spliced.remove('d')
        embed = discord.Embed(title = "Your rolls are:",Color = 0x00FF00)
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
        embed = discord.Embed(title = "Your rolls are:",Color = 0x00FF00)
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













