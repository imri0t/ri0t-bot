'''cog: basic tools for bot maintenance'''
from asyncio import sleep

import discord as d 
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Maintenance():
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.name = kwargs.get('username')

    @commands.command(pass_context=True)
    async def reload(self, ctx, *, extension_name: str):
        '''a command used to reload cogs without rebooting the bot
        (should not be reloaded)'''
        try:
            self.bot.unload_extension(extension_name)
            self.bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await self.bot.say('```py\n{}: {}```'.format(type(e), __name__))
            return
        await self.bot.say('{} has been reloaded\n '.format(extension_name))

    @commands.command(pass_context=True)
    @commands.has_permissions(Administrator=True)
    async def load(self, ctx, *, extension_name: str):
        '''a command used to load in new extensions/cogs without rebooting the bot'''
        try:
            self.bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await self.bot.say('```py\n{}: {}```'.format(type(e), __name__))
            return
        await self.bot.say('{} has been loaded\n '.format(extension_name))

    @commands.command(pass_context=True,  aliases=['Link', 'LINK'])
    async def link(self, ctx):
        '''a command that sends a link to add the bot to other servers'''
        _link = 'https://discordapp.com/oauth2/authorize?client_id=422901925034459147&permissions=8&scope=bot'
        embed = d.Embed(
            title='make sure you have permission to add bots before adding me to your server',
            description=_link,
            color=0x3f1c72)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True, aliases=['TroubleShoot', 'ts', 'TS'])
    @commands.cooldown(1,45,BucketType.user)
    async def troubleshoot(self, ctx, *querie:str):
        '''a command for sending a direct message to im.ri0t about bot queries'''
        ri0t_id = await self.bot.get_user_info(313168485591154688)
        text = ' '.join(querie)
        
        await self.bot.say('your message has been sent')

        embed = d.Embed(
            title='query received from **{}**'.format(ctx.message.author),
            description='{}'.format(text),
            color=0xffffff)
        await self.bot.send_message(ri0t_id, embed=embed)

def setup(bot):
    '''cog setup'''
    bot.add_cog(Maintenance(bot))
    print('maintenance command ready')
