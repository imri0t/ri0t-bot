'''cog: commands using the list utility'''
import random
import asyncio
import os

import discord as d
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

from utilities import lists

class ListCommands():
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.name = kwargs.get('username')
    
    @commands.command(pass_context=True, aliases=['Bye', 'BYE', 'goodbye', 'Goodbye', 'GoodBye', 'GOODBYE'])
    async def bye(self, ctx, *, member: d.Member = None):
        '''a basic goodbye command'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            gbye = random.choice(lists.bye)
            await self.bot.say(gbye)
            return

        if member.id == '422901925034459147':
            await self.bot.say('I\'m not going anywhere though')
        elif member.id == ctx.message.author.id:
            await self.bot.say('where are you going?\n can\'t just say bye to yourself')
        elif member.id == '313168485591154688':
            await self.bot.say('later dad!')
        else:
            gbye_mention = random.choice(lists.byeMention)
            await self.bot.say(gbye_mention.format(member.display_name))

    @commands.command(aliases=['CHOOSE', 'Choose'])
    async def choose(self, *choices: str):
        '''a command used to choose between different options'''
        #split choices with , using roll as ref
        rand_line = random.choice(lists.botRandLine)
        await self.bot.say(rand_line + ' __'+random.choice(choices)+'__')

    @commands.command(aliases=['8ball', '8Ball', '8BALL'])
    @commands.cooldown(1,5,BucketType.user)
    async def eightball(self, question: str):
        '''an 8ball command that gives random output'''
        await self.bot.say(random.choice(lists.eightBall))

    @commands.command(pass_context=True, aliases=['f', 'F'])
    async def _f(self, ctx, *, member: d.Member = None):
        '''a basic command that gives a random f message'''
        await self.bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.3)
        if member is None:
            respect = random.choice(lists.respect)
            await self.bot.say(respect)
            return

        if member.id == '422901925034459147':
            await self.bot.say('gimme an f spam y\'all')
        else:
            respect = random.choice(lists.respect)
            await self.bot.say(respect)
            return

    @commands.command(pass_context=True, aliases=['Goodmorning', 'GOODMORNING', 'morning', 'Morning', 'MORNING', 'gm', 'GM'])
    async def goodmorning(self, ctx, *, member: d.Member = None):
        '''a basic goodmorning command'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            gmorn = random.choice(lists.morning)
            await self.bot.say(gmorn)
            return

        if member.id == '422901925034459147':
            await self.bot.say('good morning to you too')
        elif member.id == ctx.message.author.id:
            await self.bot.say('nobody to say goodmorning to you?\nthat\'s lowkey sad, dude')
        elif member.id == '313168485591154688':
            await self.bot.say('g\' morning dad')
        else:
            morning_mention = random.choice(lists.morningMention)
            await self.bot.say(morning_mention.format(member.display_name))

    @commands.command(pass_context=True, aliases=['Goodnight', 'GOODNIGHT', 'night', 'Night', 'NIGHT', 'gn', 'GN'])
    async def goodnight(self, ctx, *, member: d.Member = None):
        '''a basic goodnight command'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            night = random.choice(lists.night)
            await self.bot.say(night)
            return

        if member.id == '422901925034459147':
            await self.bot.say('good night, friend')
        elif member.id == ctx.message.author.id:
            await self.bot.say('saying goodnight to yourself is pretty weird dude')
        elif member.id == '313168485591154688':
            await self.bot.say('night dad')
        else:
            night_mention = random.choice(lists.nightMention)
            await self.bot.say(night_mention.format(member.display_name))

    @commands.command(pass_context=True, aliases=['hbd', 'HBD', 'HAPPYBIRTHDAY', 'Happybirthday'])
    async def happybirthday(self, ctx, *, member: d.Member = None):
        '''a basic command that gives a random happy birthday message'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            await self.bot.say('so who\'s birthday is it then?')
            return

        if member.id == '422901925034459147':
            await self.bot.say('I\'ve never been born tho')
        elif member.id == '313168485591154688':
            await self.bot.say('Happy Birthday dad!')
        else:
            choice = random.choice(lists.bDayMessage)
        await self.bot.say(choice.format(member.display_name))

    @commands.command(pass_context=True, aliases=['Hello', 'HELLO', 'hi', 'Hi', 'HI', 'hey', 'Hey', 'HEY'])
    async def hello(self, ctx, *, member: d.Member = None):
        '''a basic greeting command'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            greeting = random.choice(lists.greetNoMention)
            await self.bot.say(greeting)
            return

        if member.id == '422901925034459147':
            await self.bot.say('hi.. me?')
        elif member.id == ctx.message.author.id:
            await self.bot.say('trying to say hi to yourself? Kinda weird, dude')
        elif member.id == '313168485591154688':
            await self.bot.say('HI DAD!')
        else:
            greet_mention = random.choice(lists.greetMention)
            await self.bot.say(greet_mention.format(member.display_name))

    @commands.command(pass_context=True, aliases=['Insult', 'INSULT'])
    async def insult(self, ctx, *, member: d.Member = None):
        '''a command that sends random insults'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            await self.bot.say('tell me who to insult, dingus')
            return

        if member.id == '422901925034459147':
            await self.bot.say('can\'t insult perfection lol')
        elif member.id == '313168485591154688' and member.id == ctx.message.author.id:
            await self.bot.say('why are you asking me to insult you, dude? Lol')
        elif member.id == ctx.message.author.id:
            await self.bot.say('soooooo you\'re asking me to insult you? That\'s just you insulting yourself, dude.')
        elif member.id == '313168485591154688':
            insult = random.choice(lists.insultDad)
            await self.bot.say(insult.format(member.display_name))
        else:
            insult = random.choice(lists.insults)
            await self.bot.say(insult.format(member.display_name))

    @commands.command(pass_context=True, aliases=['Kill, KILL'])
    async def kill(self, ctx, *, member: d.Member = None):
        '''a basic command that sends random kill messages'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            await self.bot.say('I\'ll just kill you if you don\'t mention someone')
            return

        if member.id == '422901925034459147':
            choice = random.choice(lists.killSelf)
            await self.bot.say(choice)
        elif member.id == '313168485591154688' and member.id == ctx.message.author.id:
            await self.bot.say('I\'m not killing you dad lol')
        elif member.id == ctx.message.author.id:
            await self.bot.say('Who do I look like? Jack Kevorkian? No assisted suicide lol')
        elif member.id == '313168485591154688':
            choice = random.choice(lists.killDad)
            await self.bot.say(choice)
        else:
            choice = random.choice(lists.killReply)
            await self.bot.say(choice.format(member.display_name))

    @commands.command(pass_context=True, aliases=['LOL', 'Lol'])
    async def lol(self, ctx, *, member: d.Member = None):
        '''a command Sany rode my ass about'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            lol = random.choice(lists.LOL)
            await self.bot.say(lol)
            return

        if member.id == '422901925034459147':
            await self.bot.say('why do you lol at me?')
        else:
            await self.bot.say('{0} {1}'.format(member.mention, random.choice(lists.LOL)))

    @commands.command(pass_context=True, aliases=['LOVE', 'Love', 'luv', 'LUV', 'Luv'])
    async def love(self, ctx, *, member: d.Member = None):
        '''a basic command that sends a random love message'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            love_message = random.choice(lists.loveNoMention)
            await self.bot.say(love_message)
            return

        if member.id == '422901925034459147':
            await self.bot.say('I love me too')
        elif member.id == ctx.message.author.id:
            love_self = random.choice(lists.selfLove)
            await self.bot.say(love_self.format(member.display_name))
        else:
            love_mention = random.choice(lists.loveMsg)
            await self.bot.say(love_mention.format(member.display_name))

    @commands.command(pass_context=True, aliases=['MOTIVATE', 'Motivate'])
    async def motivate(self, ctx):
        '''a basic command that sends a random motivational message'''
        await self.bot.send_typing(ctx.message.channel)
        motivate_message = random.choice(lists.motivateLog)
        embed = d.Embed(
            color=0x000000)
        embed.add_field(name='Quote', value=motivate_message)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True, aliases=['name', 'Name', 'NAME'])
    async def _name(self, ctx, *, member: d.Member = None):
        '''a basic command that gives a random set of words for  names'''
        await self.bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.3)
        name_1 = random.choice(lists.nOne)
        name_2 = random.choice(lists.nTwo)
        name_3 = random.choice(lists.nThree)

        name = name_1 + ' ' + name_2 + ' ' + name_3

        if member is None:
            member = ctx.message.author
            no_mention = random.choice(lists.sayNoMention).format(member.display_name)
            await self.bot.say(no_mention + ' __{}__'.format(name))
            return
        if member.id == '422901925034459147':
            await self.bot.say('my name is ri0t-bot lol')
        else:
            mention = random.choice(lists.sayMention).format(member.display_name)
            await self.bot.say(mention + ' ' + name)

    @commands.command(pass_context=True, aliases=['Oof', 'OOF'])
    async def oof(self, ctx):
        '''a basic oof command'''
        await self.bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.3)
        choice = random.choice(lists.oof)
        await self.bot.say(choice)

    @commands.command(pass_context=True, aliases=['p', 'P', 'Patrol'])
    async def patrol(self, ctx, *, member: d.Member = None):
        '''pussy patrol'''
        if member is None:
            await self.bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.3)
            await self.bot.say('who\'s trying to get pussy though?')
        elif member.id == ctx.message.author.id:
            await self.bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.3)
            await self.bot.say('everyone, look, **{}** is trying to fuck themselves again'.format(member.display_name))
        elif member.id == '422901925034459147':
            await self.bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.3)
            await self.bot.say('I\'m not trying to fuck anyone lmao')
        else:
            pussy = random.choice(lists._p)
            await self.bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.3)
            await self.bot.say(pussy.format(member.display_name))

    @commands.command(pass_context=True, aliases=['Rip', 'RIP'])
    async def rip(self, ctx):
        '''a basic rip command'''
        await self.bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.3)
        choice = random.choice(lists.ripMessage)
        await self.bot.say(choice)

    @commands.command(pass_context=True, aliases=['ShowerThoughts', 'st', 'ST'])
    async def showerthoughts(self, ctx):
        '''sends a random shower thought'''
        await self.bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.3)
        choice = random.choice(lists.dumbStuff)
        await self.bot.say(choice)

def setup(bot):
    '''cog setup'''
    bot.add_cog(ListCommands(bot))
    print('list commands ready')
