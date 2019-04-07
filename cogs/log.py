'''cog: error handler'''
import traceback
import sys

from discord.ext import commands

class LOG():
    def __init__(self, bot):
        self.bot = bot

    async def cmd_err(self, ctx, error):
        '''error checking handler'''
        if hasattr(ctx.command, 'on_error'):
            return
        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            await self.bot.say('I don\'t think I have that command')
            return
        if isinstance(error, commands.NoPrivateMessage):
            try:
                await self.bot.send_message(ctx.message.author, '{} can\'t be used as pm'.format(ctx.command))
                return
            except:
                pass
        print('Ignoring exception in command {}'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(bot):
    bot.add_cog(LOG(bot))
    print('error logging active')
