'''cog: bot update info'''
import discord
from discord.ext import commands

class PatchNotes(): # pylint: disable=too-few-public-methods
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['PatchNotes', 'pn', 'PN'])
    async def patchnotes(self, ctx):
        '''command code'''
        await self.bot.say('I\'ve sent you my patch notes information')
        embed = discord.Embed(
            title='Patch Notes',
            description='Here are my patch notes! All my released development info is right here!',
            color=0x23bc59)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        embed.add_field(name='__v0.0.5.5__', value='-added `-mouse` command (you\'re welcome pams)\n-the command `-ts` can be used to send troubleshooting info to im.ri0t\n-a queue for the music cog was made (finally)\n-updates made to dependencies of core functions (i.e. FFMpeg update)\n\n-**unfortunate bug involving discord API causing soft resets and many issues with music cog, a switch to the 1.0.0 rewrite instead of the 0.16.6 version of the API will be made eventually to attempt to remedy this issue**', inline=False)
        embed.add_field(name='__v0.0.5.3__', value='-I no longer tag people with tagged commands\n-my text files were edited to support no more double tags\n-major overhauls to my source code ~~I feel so pythonic now~~\n-you can add me to servers by using `-link`\n-added uwu command\n-added shower thoughts command (I need more shower thoughts, please send some to im.ri0t)\n-my slot machine game looks way better now!')
        embed.add_field(name='__v0.0.5.2__', value='-no u function added\n-lol function added (you\'re welcome sany)\n-~~this doesn\'t really affect anyone other than me but~~ the terminal now has colored messages\n-~~also a little something something for myself~~ all cogs have been consolidated to contain like commands, reducing the number of cogs (this affects the amount of entries available for my reload command)', inline=False)
        embed.add_field(name='__v0.0.5.1__', value='-various tweaks made to the code\n-added tmyk function\n-added tkn\n-added bye function\n-added goodmorning function\n-added goodnight function\n', inline=False)
        embed.add_field(name='__v0.0.5.0__', value='-added hall function to list all commands and their shortcuts\n-format changes to the slots function\n-optimizations made to slots function\n-**BOT CAN NOW SEND PICTURES AND GIFS**\n-added dog function\n-added cat function\n-adjusted command permissions\n-exploring possible local .mp3 player\n-~~seriously doesn\'t matter but I think it\'s cool~~ *typing* from the bot shows up\n-~~unsuccessful~~ attempts made toward leveling functionality\n-~~nobody cares but~~ bug fixes and syntax adjustments made to code', inline=False)
        embed.add_field(name='__v0.0.4.7__', value='-spelling corrections(finally)\n-added early rendition of slot machine\n-added oof command\n-~~nobody cares but~~ syntax and spelling errors have been smoothed out (mostly)\n-I\'m sorry, did someone say... **MORE QUOTES?** (additions to the -motivate command)')
        embed.add_field(name='__v0.0.4.5__', value='-began development for administrative commands (clear command now requires permissions to use)\n-added choice function (still under development)\n-added load and reload functions (less disconnecting from discord for me!)\n-added love function\n-minor fixes and adjustments\n-*more quotes* (additions to -motivate log)', inline=False)
        embed.add_field(name='__v0.0.4.3__', value='-added clear function\n-minor fixes and adjustments', inline=False)
        embed.add_field(name='__v0.0.4.2__', value='-MORE QUOTES (additions to -motivate log)\n-added insult function\n-~~not important but~~ im.ri0t uses the Atom IDE to write code now!\n-**FINALLY IMPROVED THE HELP FUNCTION** (use -h to see)', inline=False)
        embed.add_field(name='__v0.0.4.0__', value='-~~not important but~~ full code overhaul (adjusted all code using .json format files)\n-added Name command\n-added Motivate command\n-added 8ball command\n-adjusted Music functionality (bot now joins voice channel when -play is used)', inline=False)
        embed.add_field(name='__v0.0.3.2__', value='-adjusted music cog', inline=False)
        embed.add_field(name='__v0.0.3.1__', value='-fixed help function (-h)\n-bot now PM\'s help info\n-added patch notes information\n-added pause command for music function', inline=False)
        embed.add_field(name='__v0.0.3.0__', value='-~~nobody cares but~~ proper structure for cogs achieved', inline=False)
        embed.add_field(name='__v0.0.2.2__', value='-added hello function-added f function\n', inline=False)
        embed.add_field(name='__v0.0.2.1__', value='-added roll function', inline=False)
        embed.add_field(name='__v0.0.2.0__', value='-added music function', inline=False)
        embed.add_field(name='__v0.0.1.0__', value='-base code', inline=False)
        embed.set_footer(text='More updates coming in the near future. Please direct any questions, concerns, and/or requests to im.ri0t, thank you!')
        await self.bot.send_message(ctx.message.author, embed=embed)

def setup(bot):
    '''cog setup'''
    bot.add_cog(PatchNotes(bot))
    print('patch notes command ready')
