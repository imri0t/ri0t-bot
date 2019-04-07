'''bot: made by im.ri0t
        any questions should be sent to im.ri0t
'''
import os
import sys
from asyncio import sleep
from random import randint, choice

import discord as d
from discord.ext import commands

from termcolor import cprint
try:
    import colorama
    colorama.init()
except ImportError:
    pass

STARTUP = ['annoy', 'basic_replies', 'games', 'help', 'log', 'maintenance', 
           'misc', 'music', 'patch_notes', 'pics'
          ]

bot = commands.Bot(command_prefix='-', description='personal general use bot \nwritten by im.ri0t') # *
bot.remove_command('help')

class Main():
    def _init_(self, bot):
        self.bot = bot

if __name__ == '__main__':
    sys.path.insert(1, os.getcwd() + '/cogs/')
    for extension in STARTUP:
        try:
            bot.load_extension(extension)
        except (AttributeError, ImportError) as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            cprint('extension error {}\n{}'.format(extension, exc), 'red')

def rand_task():
    '''random condition picker'''
    tasks = [
        'playing', 'listening', 'watching', 'streaming'
            ]
    return choice(tasks)

# 0: playing   1: streaming(include url)   2: listening to   3: watching
async def status_task():  # pylint: disable=too-many-statements
    '''random task looper'''
    while True:
        _play = [
            'with your waifu', 'with your emotions', 'with a dirty girl',
            'with your files', 'in the Deep Web', 'something dumb',
            'with your private parts'
            ]
        _stream = [
            'hentai', 'twitch thots', 'my face reveal', 'your personal info',
            'my sex tape', 'your girl\'s nudes'
            ]
        _listen = [
            'the dark lords', 'some fat beatsies', 'my fire playlist',
            'audio books', 'some sad stuff', 'innocent screaming'
            ]
        _watch = [
            'the sun', 'vine compilations', 
            'for steam sales'
            ]

        status = rand_task()
        if status == 'playing':
            _name = choice(_play)
            _type = 0
            _url = None
        elif status == 'streaming':
            _name = choice(_stream)
            _type = 1
            _url = 'https://www.twitch.tv/imri0t'
        elif status == 'listening':
            _name = choice(_listen)
            _type = 2
            _url = None
        elif status == 'watching':
            _name = choice(_watch)
            _type = 3
            _url = None
        await bot.change_presence(game=d.Game(name='for -help', type=3))
        await sleep(45)
        await bot.change_presence(game=d.Game(name=_name, url=_url, type=_type))
        await sleep(25)

@bot.event
async def on_ready():
    '''printed in console when started'''
    cprint('------------------------------------------------------------------------------------------------------------------------', 'cyan')
    print(bot.user.name)
    print(bot.user.id)
    print('time to fuck bitches and eat frosted flakes')
    cprint('https://discordapp.com/api/oauth2/authorize?client_id=422901925034459147&permissions=0&scope=bot \n', 'red')
    cprint('------------------------------------------------------------------------------------------------------------------------', 'cyan')
    await bot.loop.create_task(status_task())

@bot.event
async def on_member_join(member):
#change the channel ID for other servers!!!
    channel = member.server.get_channel('421018068811120664')
    welcome_lib = ['glhf', 'hope you enjoy the stay', 'kick your feet up', 'don\'t drink the punch']
    welcome = choice(welcome_lib)
    fmt = ('Welcome to the server, **{0}**, if you want to know my commands use -help and I\'ll pm you, {1}'.format(member.display_name, welcome))
    await bot.send_message(channel, fmt.format(member, member.server))

@bot.event
async def on_member_remove(member):
    '''mentions members who leave'''
#change the channel ID for other servers!!!
    fmt = '**{0}** has left us.'
    channel = member.server.get_channel('421018068811120664')
    await bot.send_message(channel, fmt.format(member.display_name, member.server))

bot.run('')

# *
# many thanks to all the folks from github, stack overflow, and reddit 
# who have helped me get this bot to the working condition it is at now
