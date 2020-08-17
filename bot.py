import discord
from discord.ext import commands # Key to making commands.

import datetime
import requests
import random
import time

client = commands.Bot(command_prefix = '-') # Setting the command prefix for the commands.

client.remove_command('help')

@client.event # Basic Event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='bot.py'))
    channel = client.get_channel(744995904381124729)
    await channel.send(f'I am now online and ready to go!  (•◡•) /')
    print('Now online!')

@client.event
async def on_member_join(member): # When a member joins
    channel = client.get_channel(744973486115651735)
    await channel.send(f'A player has joined! ✍(◔◡◔)')

    embed = discord.Embed(
    title = 'Welcome to your Class!',
    description = 'I am your friendly neigborhood bot! I am here to help you with everyday needs.\n\nTo get a better idea of what I can do go to your class and type -help\nI hope you have a great experiance with Bottega!',
    colour = discord.Colour.blue()
    )

    embed.set_footer(text='Made with ❤️ by Bottega students.')
    embed.set_thumbnail(url='https://avatars1.githubusercontent.com/u/34694091?s=280&v=4')
    embed.add_field(name='Your Teacher', value='Benjamin Nicklaus')
    embed.add_field(name='Days Off', value='July 24th | Pioneer Day\nSeptember 7th | Labor Day')

    await member.send(embed=embed)

# Get help
@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Commands',
        description = 'Full list of commands.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Made with ❤️ by Bottega students.')
    embed.set_thumbnail(url='https://avatars1.githubusercontent.com/u/34694091?s=280&v=4')
    embed.add_field(name='Clearing Chat', value='-clear | -clr', inline=False)
    embed.add_field(name='Random Fact', value='-fact | -random-fact', inline=False)
    embed.add_field(name='Get a amazing Emoji', value='-emoji | -smile', inline=False)
    embed.add_field(name='Magic 8 Ball', value='-m8b | -magic (QUESTION)', inline=False)
    embed.add_field(name='Bot tells a joke', value='-joke', inline=False)
    embed.add_field(name='set a timer', value='-timer (time in minutes)', inline=False)
    embed.add_field(name='Check the weather', value='-weather | -temp | temperature (ZIPCODE)', inline=False)

    await ctx.send(embed=embed)

# Clear messages
@client.command(aliases=['clr'])
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

# Get magic 8 ball answer
@client.command(aliases=['magic'])
async def m8b(ctx):
    answers = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes - definitely.",
        "You may rely on it."
    ]
    await ctx.send(random.choice(answers))

# Get random fact
@client.command(aliases=['fact'])
async def random_fact(ctx):
    r = requests.get('https://uselessfacts.jsph.pl/random.json?language=en').json()
    await ctx.send(f'Your random fact is!\n{r["text"]}')

# Get joke
@client.command()
async def joke(ctx):
    responses = [
        "How did the programmer die in the shower? He read the shampoo bottle instructions: Lather. Rinse. Repeat.",
        "A man is smoking a cigarette and blowing smoke rings into the air.  His girlfriend becomes irritated with the smoke and says, “Cant you see the warning on the cigarette pack?  Smoking is hazardous to your health!” To which the man replies, “I am a programmer.  We don’t worry about warnings; we only worry about errors.”",
        "http://www.devtopics.com/wp-content/uploads/2008/05/comic.jpg",
        "https://www.thecoderpedia.com/wp-content/uploads/2020/06/Programming-Life-Strongest-Programmer-937x1024.jpg",
        "https://miro.medium.com/max/700/1*prwmwbZl1XJnPfzU41_AxA.jpeg",
        "A guy walks into a bar and asks for 1.4 root beers. The bartender says \"I\'ll have to charge you extra, that's a root beer float\". The guy says \"In that case, better make it a double.\"",
        "How many programmers does it take to change a lightbulb? None, that's a hardware problem",
        "What's the object-oriented way of becoming wealthy? Inheritance",
        "Why did the programmer quit his job? Because he didn't get arrays",
        "What is the most used language in programming? Profanity",
    ]
    await ctx.send(random.choice(responses))

# Get smiley face
@client.command(aliases=['smile'])
async def emoji(ctx):
    smiley_faces = [
        '༼ つ ◕_◕ ༽つ',
        '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)',
        'ಠ_ಠ',
        '( ͡°╭͜ʖ╮͡° )',
        '┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴',
        '(◕‿◕✿)',
        '♪~ ᕕ(ᐛ)ᕗ',
        '♥‿♥',
        ':)',
        ':D',
        ':]',
        '༼ ºل͟º ༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽',
        '☼.☼',
        '^̮^',
        '(~_^)',
        '✍(◔◡◔)',
        '(✖╭╮✖)',
        '( ͡°👅 ͡°)',
        '༼ﾉຈل͜ຈ༽ﾉ︵┻━┻'
    ]
    await ctx.send(random.choice(smiley_faces))

# Get weather
@client.command(aliases=['weather', 'temp', 'temperature'])
async def current_temp(ctx, zip_code, country_code="us"):
    api_key = "92d9b44cceb8ddfd0b87c7339e23b367"
    temp_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}").json()
    city_name = temp_request["name"]
    condition = temp_request["weather"][0]["main"]
    temp_farenheit = ((temp_request["main"]["temp"]) - 273.15) * (9/5) + 32
    farenheit = int(temp_farenheit)
    temp_feels_like = ((temp_request["main"]["feels_like"]) - 273.15) * (9/5) + 32
    actual_feels_like = int(temp_feels_like)
    humidity = temp_request["main"]["humidity"]
    temp_wind = temp_request["wind"]["speed"] * 2.237
    actual_wind = "{:.2f}".format(temp_wind)

    await ctx.send(f"In {city_name}, the current condition is: {condition}.\nThe temperature is {farenheit}°F but it feels like {actual_feels_like}°F.\nThere is {humidity}% humidity and a wind speed of {actual_wind}mph.")

# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         t -= 1
#     print('Goodbye!\n')

# countdown(10)

client.run('NzQ0NzU3ODM3NDYwNDA2MzMy.Xzn3yQ.IkMdHti9Znrb58yWpVNymYw8YMw') # Inside is the key & finishes the connection to discord.