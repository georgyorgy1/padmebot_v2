import discord
import asyncio
import datetime
import random
import time

bot = discord.Client()
start_time = time.time()

@bot.event
async def about(message):
    string = "```" + "\n" + "PadmeBot v2.0 Beta. Copyright Darth Squidward" + "\n" + "See m!commands for commands" + "\n" + "```"
    await bot.send_message(message.channel, string)
    print(str(datetime.datetime.now()) + ": " + "m!about triggered")

@bot.event
async def uptime(message):
    string = "```" + "\n" + "Uptime (in seconds) is: " + str(int(time.time() - start_time)) + "\n" + "```"
    await bot.send_message(message.channel, string)
    print(str(datetime.datetime.now()) + ": " + "m!uptime triggered")
    
@bot.event
async def random_number(message):
    num = random.randint(0, 2147483647)
    string = "```" + "\n" + "Here's your number: " + str(num) + "\n" + "```"
    await bot.send_message(message.channel, string)
    print(str(datetime.datetime.now()) + ": " + "m!random triggered")

@bot.event
async def check_datetime(message):
    current_datetime = time.strftime("%A, %B %d, %Y %I:%M:%S %p")
    string = "```" + "\n" + "Current date and time (GMT 8:00+): " + str(current_datetime) + "\n" + "```"
    await bot.send_message(message.channel, string)
    print(str(datetime.datetime.now()) + ": " + "m!dt/m!time triggered")

@bot.event
async def aesthetics(message):
    aesthetic = open('aesthetics.txt')
    await bot.send_message(message.channel, random.choice(aesthetic.readlines()))
    aesthetic.close()
    print(str(datetime.datetime.now()) + ": " + "m!aesthetics triggered")

@bot.event
async def test_function(message):
    await bot.send_message(message.channel, "returning message")
    print(str(datetime.datetime.now()) + ": " + "Test function triggered")

@bot.event
async def print_commands(message):
    string = open('commands.txt')
    await bot.send_message(message.channel, string.read())
    string.close()
    print(str(datetime.datetime.now()) + ": " + "m!commands triggered")

@bot.event
async def send_nudes(message):
    await bot.send_message(message.channel, "Feature coming soon")
    print(str(datetime.datetime.now()) + ": " + "m!nudes triggered")

@bot.event
async def on_message(message):
    if message.content.startswith('m!loltest') and str(message.author.id) == str(bot.user.id):
        await test_function(message) #test function
        
    if message.content.startswith('m!aesthetics'):
        await aesthetics(message) #prints aestheics. From AestheticsBot and PadmeBot

    if message.content.startswith('m!dt'):
        await check_datetime(message) #checks datetime lol

    if message.content.startswith('m!time'):
        await check_datetime(message) #checks datetime also lol

    if message.content.startswith('m!random'):
        await random_number(message) #generates a random 32-bit number (from 1 to the 32-bit limit)

    if message.content.startswith('m!uptime'):
        await uptime(message) #check uptime

    if message.content.startswith('m!about'):
        await about(message) #about selfbot

    if message.content.startswith('m!commands'):
        await print_commands(message) #print commands

    if message.content.startswith('m!nudes'):
        await send_nudes(message) #sends nudes

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='m!commands for commands'))
    print(str(datetime.datetime.now()) + ": " + "Welcome " + str(bot.user))
    print(str(datetime.datetime.now()) + ": " + "Current date and time: " + str(datetime.datetime.now()))
        
def main():
    credentials = open('creds.txt')
    auth = []
    
    with credentials as f:
        auth = f.read().splitlines()
    
    credentials.close()
    
    try:
        print(str(datetime.datetime.now()) + ": " + "Starting PadmeBot v2.0. Please wait...")
        bot.run(auth[0]) #token 
        auth = ""
            
    except discord.errors.LoginFailure:
        error_string = "Your token is either invalid or empty. Please replace the token in creds.txt with a valid one. Quitting..."
        print(str(datetime.datetime.now()) + ": " + error_string)
        quit()

#go to main()
main()