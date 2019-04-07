'''cog: all bot games'''
import random

import discord as d
from discord.ext import commands
from discord import errors

class Games():
    def __init__(self, bot): # pylint: disable=too-few-public-methods
        self.bot = bot

    @commands.command(pass_context=True, aliases=['Spin', 'SPIN', 'slot', 'Slot', 'SLOT', 'slots', 'Slots', 'SLOTS'])
    async def spin(self, ctx):
        '''slot machine'''
        reel = [':cherries:', ':tangerine:', ':lemon:', ':pineapple:', ':apple:', ':green_apple:', ':grapes:', ':strawberry:']

        slot_a = reel[random.randint(0,7)]
        slot_b = reel[random.randint(0,7)]
        slot_c = reel[random.randint(0,7)]
        slot_d = reel[random.randint(0,7)]
        slot_e = reel[random.randint(0,7)]
        slot_a1 = reel[random.randint(0,7)]
        slot_b1 = reel[random.randint(0,7)]
        slot_c1 = reel[random.randint(0,7)]
        slot_d1 = reel[random.randint(0,7)]
        slot_e1 = reel[random.randint(0,7)]
        slot_a2 = reel[random.randint(0,7)]
        slot_b2 = reel[random.randint(0,7)]
        slot_c2 = reel[random.randint(0,7)]
        slot_d2 = reel[random.randint(0,7)]
        slot_e2 = reel[random.randint(0,7)]

        reels = [slot_a, slot_b, slot_c, slot_d, slot_e]
        reels1 = [slot_a1, slot_b1, slot_c1, slot_d1, slot_e1]
        reels2 = [slot_a2, slot_b2, slot_c2, slot_d2, slot_e2]

        reels = [slot_a, slot_b, slot_c, slot_d, slot_e]

        if slot_a == slot_b and slot_b == slot_c and slot_c == slot_d and slot_d == slot_e:
            result = 'JACKPOT'
        elif slot_a == slot_b and slot_b == slot_c and slot_c == slot_d or slot_b == slot_c and slot_c == slot_d and slot_d == slot_e:
            result = '4 in a row!'
        elif slot_a == slot_b and slot_b == slot_c and slot_d == slot_e:
            result = 'triple double, sweet'
        elif slot_a == slot_b and slot_c == slot_d and slot_d == slot_e:
            result = 'double triple, sweet'
        elif slot_a == slot_b and slot_b == slot_c or slot_b == slot_c and slot_c == slot_d or slot_c == slot_d and slot_d == slot_e:
            result = '3 in a row, pretty good'
        elif slot_a == slot_b and slot_c == slot_d or slot_b == slot_c and slot_d == slot_e or slot_a == slot_b and slot_d == slot_e:
            result = '2 pairs, nice'
        elif slot_a == slot_b or slot_b == slot_c or slot_c == slot_d or slot_d == slot_e:
            result = '2 in a row, not bad'
        else:
            result = 'you lose'
        embed = d.Embed(
            color=0xc64519)

        re = ' | '.join(reels1)
        re1 = ' | '.join(reels)
        re2 = ' | '.join(reels2)
        embed.add_field(name='ri0t slots', value='{}\n{} <-\n{}'.format(re, re1, re2))
        embed.set_footer(text='{}'.format(result))
        await self.bot.say(embed=embed)

    @commands.command(aliases=['Roll', 'ROLL'])
    async def roll(self, dice: str):
        '''dice roll command'''
        try:
            rolls, limit = map(int, dice.split('d'))
        except ValueError:
            await self.bot.say('NdN format plz thank')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)

    @commands.command(pass_context=True, aliases=['RPS'])
    async def rps(self, ctx, play: str):
        '''rock paper scissors game'''
        _plays = [
            'rock', 'paper', 'scissors'
        ]
        comp = _plays[random.randint(0,2)]
        user = play.lower() 

        if user == comp:
            await self.bot.say(comp+'\nwe tied, I guess')
        elif user == 'rock':
            if comp == 'paper':
                await self.bot.say(comp+'\nI won, loser')
            else:
                await self.bot.say(comp+'\nyou won lol')
        elif user == 'paper':
            if comp == 'scissors':
                await self.bot.say(comp+'\nI won, loser')
            else:
                await self.bot.say(comp+'\nyou won lol')
        elif user == 'scissors':
            if comp == 'rock':
                await self.bot.say(comp+'\nI won, loser')
            else:
                await self.bot.say(comp+'\nyou won lol')
        else:
            await self.bot.say('that\'s not how you play rock paper scissors, dingus')

def setup(bot):
    '''cog setup'''
    bot.add_cog(Games(bot))
    print('games are ready')
