'''cog: commands using pictures'''
from random import choice
import os

import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

from utilities import lists

class Pictures():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['Dog', 'DOG', 'dogs', 'Dogs', 'DOGS'])
    @commands.cooldown(1,3,BucketType.user)
    async def dog(self, ctx):
        '''send pictures of dogs'''
        os.chdir(r'D:\Code-Dev\Pyhthon\DiscordStuff\Bots\ri0tbot\ri0t-bot_current_version\utilities\pets')
        doggo = choice(lists.DOGGOS)
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, doggo)

    @commands.command(pass_context=True, aliases=['Cat', 'CAT', 'cats', 'Cats', 'CATS'])
    @commands.cooldown(1,3,BucketType.user)
    async def cat(self, ctx):
        '''send pictures of cats'''
        os.chdir(r'D:\Code-Dev\Pyhthon\DiscordStuff\Bots\ri0tbot\ri0t-bot_current_version\utilities\pets')
        catto = choice(lists.CATES)
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, catto)

    @commands.command(pass_context=True, aliases=['MICE', 'mouse', 'MOUSE'])
    @commands.cooldown(1,3,BucketType.user)
    async def mice(self, ctx):
        '''send pictures of mice'''
        #<3 u pami
        os.chdir(r'D:\Code-Dev\Pyhthon\DiscordStuff\Bots\ri0tbot\ri0t-bot_current_version\utilities\pets')
        _mice = choice(lists.MUSHKA)
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, _mice)

    @commands.command(pass_context=True, aliases=['no', 'No', 'NO', 'nou', 'NoU', 'NOU'])
    async def _no(self, ctx, *, member: discord.Member = None):
        '''no u command'''
        os.chdir(r'D:\Code-Dev\Pyhthon\DiscordStuff\Bots\ri0tbot\ri0t-bot_current_version\utilities\memes')
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            await self.bot.say('no u')
        elif member.id == '422901925034459147':
            await self.bot.say('no u {}'.format(member.display_name))
        elif member.id == ctx.message.author.id:
            await self.bot.send_file(ctx.message.channel, 'spiderman.png')
        else:
            await self.bot.say('no u {}'.format(member.display_name))

    @commands.command(pass_context=True, aliases=['TheMoreYouKnow', 'THEMOREYOUKNOW', 'tmyk', 'TMYK'])
    async def themoreyouknow(self, ctx):
        '''the more you know command'''
        os.chdir(r'D:\Code-Dev\Pyhthon\DiscordStuff\Bots\ri0tbot\ri0t-bot_current_version\utilities\memes')
        tmyk = choice(lists.TMYK)
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, tmyk)

    @commands.command(pass_context=True, aliases=['UWU'])
    async def uwu(self, ctx, *, member: discord.Member = None):
        '''sends uwu'''
        os.chdir(r'D:\Code-Dev\Pyhthon\DiscordStuff\Bots\ri0tbot\ri0t-bot_current_version\utilities\memes')
        if member is None:
            _uwu = choice(lists.uwu)
            await self.bot.send_typing(ctx.message.channel)
            await self.bot.say(_uwu)
        else:
            uwu = choice(lists._uwu)
            await self.bot.send_typing(ctx.message.channel)
            await self.bot.send_file(ctx.message.channel, uwu)

    @commands.command(pass_context=True, aliases=['YouKnowNothing', 'YOUKNOWNOTHING', 'ykn', 'YKN'])
    async def youknownothing(self, ctx):
        '''you know nothing command'''
        os.chdir(r'D:\Code-Dev\Pyhthon\DiscordStuff\Bots\ri0tbot\ri0t-bot_current_version\utilities\memes')
        ykn = choice(lists.YKN)
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.send_file(ctx.message.channel, ykn)

def setup(bot):
    '''cog setup'''
    bot.add_cog(Pictures(bot))
    print('picture commands ready')
