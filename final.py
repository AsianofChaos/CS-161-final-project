#joshua Isakson
#6/8/2021
#here is a link to the discord that i did all my testing in https://discord.gg/HA8RAB4j you should be able to use all the commands if the bot is up



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

#function recursion
#@client.command(name = 'factorial')
#async def version(message):
    #botspam = client.get_channel(851701508776525844)
    #integer = message.content
    #def factorial(intnumber):
        #if intnumber == 1:
            #return 1
        #else:
            #return(intnumber * factorial(intnumber - 1))
        
    #await botspam.send(factorial(integer))  #couldnt get this to work in time



#def factorial(intnumber):   #makes a function
        #if intnumber == 1:   #checks if the number is 1
            #return 1 #if it is the factorial is 1
        #else:  #if its not 1 than it has a factorial
            #return(intnumber * factorial(intnumber - 1))  

#integer = int(input('please input an integer:'))
#print(factorial(integer),'is the factorial of',integer) 


@client.event
async def on_message(message):
    if message.content.startswith('!'):   #if the message starts with "!" the bot will assume its a dice roll
        botspam = client.get_channel(851701508776525844)    
        content = message.content    #this gets the content of the message such as '4 d 4'
        spliced = content.split()   #splits the content into a list
        spliced.remove('!')    # removes the inital !
        spliced.remove('d')   # removes the useless d
        embed = discord.Embed(title = "Your rolls are:",color = 0x00ff00) # creates the discord embed
        dicenum = int(spliced[0])  #gets the number of dice out of the list
        diceval = int(spliced[1])  #gets the number of side out of the list
        total = 0                  # this is the initial value of all the rolls together
        while dicenum>0:  #loop runs while the number of dice left is greater than 0
            randnum = random.randint(1,diceval) #gets the random number from 1 to the number of sides on the dice
            total = total+randnum      # adds the random number to the overall value
            embed.add_field(name = 'Roll:',value = randnum,inline = False) #adds a field every time a dice gets rolled and adds the number
            dicenum -= 1           #removes a dice every time one gets rolled
        embed.add_field(name = 'Total Roll:',value = total,inline = False) #adds the total roll to the embed
        await botspam.send(embed = embed)  #sends the embed


#class thisisatestingclass:

     #hight = 20
     #length = 30
     #width = 40 


     #def example(self):
         #print(example)
#print(thisisatestingclass.hight)
#print(thisisatestingclass.length)
#print(thisisatestingclass.width)

#print(thisisatestingclass.__dict__)
#print(thisisatestingclass.__doc__)
#print(thisisatestingclass.example)


#this is what runs the bot, the long string is the bot token this is what makes this program the bot and not just a program.
client.run('ODUxNjg4NTY1NzIwNzQzOTQ2.YL76yQ.mWtpQ8bxtQ_EPUODk17fVhE0JA8') 