'''cog: miscellaneous commands'''
import os
import asyncio
import random

import discord
from discord.ext import commands

class Misc(): # pylint: disable=too-few-public-methods
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['delete', 'prune', 'Clear', 'CLEAR'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount):
        '''deletes messages'''
        channel = ctx.message.channel
        messages = []

        async for message in self.bot.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await self.bot.delete_messages(messages)

        msg = await self.bot.say('I got rid of __{} {}__ for you'.format(amount, 'message' if int(amount) == 1 else 'messages'))
        await asyncio.sleep(3)
        await self.bot.delete_message(msg)

def setup(bot):
    '''cog setup'''
    bot.add_cog(Misc(bot))
    print('misc commands ready')

#░▓▒