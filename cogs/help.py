'''cog: command list and info'''
import discord
from discord.ext import commands

class Help(): # pylint: disable=too-many-public-methods
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['h', 'H', 'Help', 'HELP', 'help1', 'Help1', 'HELP1', 'h1', 'H1'])
    async def help(self, ctx):
        '''core text for help command'''
        await self.bot.say('I\'ve sent you a PM with my help info')
        embed = discord.Embed(
            title='**Help List 1/2**',
            description='Here is list 1/2 of my commands. Use `-help2` (or `-h2` or whatever) for the extended list. Use `-h[command]` for more information on specific commands. To see all shortcuts for commands use `-hall`. My prefix: -',
            color=0x3f1c72)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        embed.add_field(name='__8ball__', value='An 8ball thingy, prepare to be mystified\n', inline=False)
        embed.add_field(name='__bye__', value='I\'ll send a random goodbye message', inline=False)
        embed.add_field(name='__cat__', value='I\'ll send a random picture of a cat that I have saved\n', inline=False)
        embed.add_field(name='__choose__', value='I\'ll make a choice for you (please check hchoose for more info)', inline=False)
        embed.add_field(name='__clear__', value='Clear a stated amount of messages\n', inline=False)
        embed.add_field(name='__dog__', value='I\'ll send a random picture of a dog that I have saved\n', inline=False)
        embed.add_field(name='__f__', value='F for respect\n', inline=False)
        embed.add_field(name='__goodmorning__', value='I\'ll say goodmorning and stuff', inline=False)
        embed.add_field(name='__goodnight__', value='I\'ll say good night and stuff', inline=False)
        embed.add_field(name='__HappyBirthday__', value='I\'ll wish the tagged user a happy birthday\n', inline=False)
        embed.add_field(name='__hello__', value='I\'ll greet some peeps\n', inline=False)
        embed.add_field(name='__insult__', value='I\'ll insult a tagged user\n', inline=False)
        embed.add_field(name='__kill__', value='I\'ll kill the tagged user\n', inline=False)
        embed.add_field(name='__link__', value='This sends a clickable link to add me to servers', inline=False)
        embed.add_field(name='__load__', value='this will make me load a specified command file', inline=False)
        embed.add_field(name='__lol__', value='I\'ll say lol and can tag people with it', inline=False)
        embed.add_field(name='__love__', value='I\'ll tell someone how much you love them', inline=False)
        embed.add_field(name='__motivate__', value='Random inspirational quote generator\n', inline=False)
        embed.add_field(name='__mouse__', value='sends a random picture of a mouse', inline=False)
        embed.add_field(name='__MusicCommands__', value='I\'ll send my command list for my music function (still under maintenance)\n', inline=False)
        embed.add_field(name='__name__', value='Random name generator\n', inline=False)
        embed.add_field(name='__no__', value='I\'ll say no u', inline=False)
        embed.add_field(name='__oof__', value='I\'ll say oof back\n', inline=False)
        embed.add_field(name='__PatchNotes__', value='Full development patch notes will be sent directly to you', inline=False)
        embed.set_footer(text='page 1/2 Please direct any questions, concerns, and/or requests to im.ri0t, thank you!')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True, aliases=['h2', 'H2', 'Help2', 'HELP2'])
    async def help2(self, ctx):
        '''part 2 of help text'''
        await self.bot.say('I\'ve sent you a PM with my help info')
        embed = discord.Embed(
            title='**Help List 2/2**',
            description='Here is list 2/2 of my commands. Use h[command] for more information on specific commands. To see all shortcuts for commands use -hall. My prefix: -',
            color=0x3f1c72)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        embed.add_field(name='__patrol__', value='I call out someone for being thirsty', inline=False)
        embed.add_field(name='__reload__', value='This will reload a specified command', inline=False)
        embed.add_field(name='__rip__', value='I\'ll say rip back\n', inline=False)
        embed.add_field(name='__roll__', value='NdN format dice roll\n', inline=False)
        embed.add_field(name='__rps__', value='rock, paper, scissors!', inline=False)
        embed.add_field(name='__showerthoughts__', value='Sends a random shower thought', inline=False)
        embed.add_field(name='__slots__', value='A basic slot machine (more coming soon™)', inline=False)
        embed.add_field(name='__tmyk__', value='You should learn something new every day', inline=False)
        embed.add_field(name='__troubleshoot__', value='send a troubleshooting querie directly to im.ri0t', inline=False)
        embed.add_field(name='__uwu__', value='Sends uwu', inline=False)
        embed.add_field(name='__ykn__', value='Sometimes you just don\'t know', inline=False)
        embed.set_footer(text='page 2/2 Please direct any questions, concerns, and/or requests to im.ri0t, thank you!')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True, aliases=['MusicCommands', 'mc', 'MC', 'MUSICCOMMANDS'])
    async def musiccommands(self, ctx):
        '''a list of commands for the music cog'''
        await self.bot.say('I\'ve sent you a PM with my music command info')
        embed = discord.Embed(
            title='Music Commands',
            description='Hi there! This is a list of all my music commands.',
            color=0xff0000)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        embed.add_field(name='__leave__', value='I\'ll leave the voice channel and clear the queue', inline=False)
        embed.add_field(name='__music__', value='I\'ll connect to the voice channel you\'re in', inline=False)
        embed.add_field(name='__pause__', value='The currently playing tunes will be paused', inline=False)
        embed.add_field(name='__play__', value='I\'ll play music you request or play it from a link (also I\'ll join your voice channel if I\'m not in one yet)', inline=False)
        embed.add_field(name='__playing__', value='I\'ll tell you what the current playing song is', inline=False)
        embed.add_field(name='__resume__', value='The paused music will continue playing', inline=False)
        embed.add_field(name='__skip__', value='A vote to skip will start, 2 votes needed to skip', inline=False)
        embed.add_field(name='__volume__', value='Change my volume (preferably somewhere between 0-100)', inline=False)
        embed.set_footer(text='This function is still under maintenance, if there are any issues please contact im.ri0t, thank you!')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True, aliases=['hall'])
    async def hall1(self, ctx):
        '''a list of commands and their shortcuts'''
        await self.bot.say('I\'ve sent you my shortcut info')
        embed = discord.Embed(
            title='Shortcut Info 1/2',
            description='Hello! This is list 1/2 of all my commands and their shortcuts.',
            color=0xa55209)
        #include command:  
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        embed.add_field(name='__8ball__', value='8ball, eightball, 8Ball, 8BALL', inline=False)
        embed.add_field(name='__bye__', value='bye, Bye, BYE, goodbye, Goodbye, GoodBye, GOODBYE', inline=False)
        embed.add_field(name='__cat__', value='cat, Cat, CAT, cats, Cats, CATS', inline=False)
        embed.add_field(name='__choose__', value='choose, Choose, CHOOSE', inline=False)
        embed.add_field(name='__clear__', value='clear, Clear, CLEAR, prune, delete', inline=False)
        embed.add_field(name='__dog__', value='dog, Dog, DOG, dogs, Dogs, DOGS', inline=False)
        embed.add_field(name='__f__', value='f, F', inline=False)
        embed.add_field(name='__goodmorning__', value='goodmorning, Goodmorning, GOODMORNING, morning, Morning, MORNING, gm, GM', inline=False)
        embed.add_field(name='__goodnight__', value='goodnight, Goodnight, GOODNIGHT, night, Night, NIGHT, gn, GN', inline=False)
        embed.add_field(name='__HappyBirthday__', value='HappyBirthday, Happybirthday, HAPPYBIRTHDAY, hbd, HBD', inline=False)
        embed.add_field(name='__hello__', value='hello, Hello, HELLO, hi, Hi, HI, hey, Hey, HEY', inline=False)
        embed.add_field(name='__insult__', value='insult, Insult, INSULT', inline=False)
        embed.add_field(name='__kill__', value='kill, Kill, KILL', inline=False)
        embed.add_field(name='__leave__', value='leave', inline=False)
        embed.add_field(name='__link__', value='link, Link, LINK', inline=False)
        embed.add_field(name='__load__', value='load', inline=False)
        embed.add_field(name='__lol__', value='lol, Lol, LOL', inline=False)
        embed.add_field(name='__love__', value='love, Love, LOVE, luv, Luv, LUV', inline=False)
        embed.add_field(name='__motivate__', value='motivate, Motivate, MOTIVATE', inline=False)
        embed.add_field(name='__mouse__', value='mouse')
        embed.add_field(name='__music__', value='music, MUSIC, join, JOIN', inline=False)
        embed.add_field(name='__MusicCommands__', value='musiccommands, MusicCommands, MUSICCOMMANDS, mc, MC', inline=False)
        embed.add_field(name='__name__', value='name, Name, NAME', inline=False)
        embed.add_field(name='__no__', value='no, No, NO, nou, NoU, NOU', inline=False)
        embed.add_field(name='__oof__', value='oof, Oof, OOF', inline=False)
        embed.add_field(name='__PatchNotes__', value='patchnotes, PatchNotes, PATCHNOTES, pn, PN', inline=False)
        embed.set_footer(text='page 1/2 (for the continued list please use `-hall2`)')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hall2(self, ctx):
        '''part 2 of the hall command'''
        embed = discord.Embed(
            title='Shortcut Info 2/2',
            description='This is list 2/2 of all my commands and their shortcuts.',
            color=0xa55209)
        embed.add_field(name='__PatchNotes__', value='patchnotes, PatchNotes, PATCHNOTES, pn, PN', inline=False)
        embed.add_field(name='__patrol__', value='patrol, Patrol, p, P', inline=False)
        embed.add_field(name='__pause__', value='pause', inline=False)
        embed.add_field(name='__play__', value='play', inline=False)
        embed.add_field(name='__playing__', value='playing', inline=False)
        embed.add_field(name='__reload__', value='reload', inline=False)
        embed.add_field(name='__resume__', value='resume', inline=False)
        embed.add_field(name='__rip__', value='rip, Rip, RIP', inline=False)
        embed.add_field(name='__roll__', value='roll, Roll, ROLL', inline=False)
        embed.add_field(name='__rps__', value='RPS', inline=False)
        embed.add_field(name='__skip__', value='skip', inline=False)
        embed.add_field(name='__slots__', value='slots, Slots, SLOTS, spin, Spin, SPIN, slot, Slot, SLOT', inline=False)
        embed.add_field(name='__showerthoughts__', value='showerthoughts, ShowerThoughts, sh, SH', inline=False)
        embed.add_field(name='__tmyk__', value='tmyk, TMYK, themoreyouknow, TheMoreYouKnow, THEMOREYOUKNOW', inline=False)
        embed.add_field(name='__troubleshoot__', value='troubleshoot, TroubleShoot, ts, TS', inline=False)
        embed.add_field(name='__uwu__', value='uwu, UWU', inline=False)
        embed.add_field(name='__volume__', value='volume, vol', inline=False)
        embed.add_field(name='__ykn__', value='ykn, YKN, youknownothing, YouKnowNothing, YOUKNOWNOTHING', inline=False)
        embed.set_footer(text='page 2/2')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def h8ball(self, ctx):
        embed = discord.Embed(
            title='__8ball__',
            description='This is an 8ball function. By asking me a question I\'ll give you a random response; *it\'s so magical!*',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hbye(self, ctx):
        embed = discord.Embed(
            title='__bye__',
            description='You can tag a user for this command, but it\'s not mandatory. I\'ll send a random good bye message.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hcat(self, ctx):
        embed = discord.Embed(
            title='__cat__',
            description='This command will make me send a random picture of a cat that I have saved in one of my subfolders (all pictures are saved in .png format)',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hchoose(self, ctx):
        embed = discord.Embed(
            title='__choose__',
            description='This function will have me choose between multiple things for you. For the time being I can only choose one word so if you try to have me choose something with two or more words (i.e. fries and burger) I\'ll only be able to pick one word from it. (i.e. fries from last example). Also you don\'t have to use a comma to separate items I choose from.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hclear(self, ctx):
        embed = discord.Embed(
            title='__clear__',
            description='**This is an admin command.**\nThis is a command to have me delete a stated number of messages. \nUse `-clear [number]` to dictate how many messages you\'d like to have me delete. I can only delete between 1 and 99 messages so keep that in mind. Also this command won\'t work on messages that are over 14 days old.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hdog(self, ctx):
        embed = discord.Embed(
            title='__dog__',
            description='This command will make me send a random picture of a cat that I have saved in one of my subfolders (all pictures are saved in .png format)',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hf(self, ctx):
        embed = discord.Embed(
            title='__f__',
            description='I\'ll respond to this commands with a random response that involves \'f in the chat,\' that\'s about it.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hgoodmorning(self, ctx):
        embed = discord.Embed(
            title='__goodmorning__',
            description='You can tag a user for this command, but it\'s not mandatory. I\'ll greet people with a good morning message.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hgoodnight(self, ctx):
        embed = discord.Embed(
            title='__goodnight__',
            description='You can tag a user for this command, but it\'s not mandatory. I\'ll send a good night message to people',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hHappyBirthday(self, ctx):
        embed = discord.Embed(
            title='__HappyBirthday__',
            description='Tag a user for this command. I\'ll respond with a random happy birthday wish.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hhello(self, ctx):
        embed = discord.Embed(
            title='__hello__',
            description='You can tag a user for this command, but it\'s not mandatory. I\'ll greet people with a random message.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hinsult(self, ctx):
        embed = discord.Embed(
            title='__insult__',
            description='Tag a user for this command. I\'ll insult the tagged user for you with a random message.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hkill(self, ctx):
        embed = discord.Embed(
            title='__kill__',
            description='Tag a user for this command. I\'ll \'kill\' the tagged user with a random message.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hlink(self, ctx):
        embed = discord.Embed(
            title='__link__',
            description='This command will get me to send a clickable link to add me to other servers. Make sure that you have permission to add bots to the server you want me in. By the way, here\'s the link:\nhttps://discordapp.com/api/oauth2/authorize?client_id=422901925034459147&permissions=0&scope=bot',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hleave(self, ctx):
        embed = discord.Embed(
            title='__leave__',
            description='If you use this command and I\'m in a voice channel then I\'ll disconnect from it and clear the queue.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hload(self, ctx):
        embed = discord.Embed(
            title='__load__',
            description='**This is an admin command.**\nThis command will load a specified command file. By using `-load [commandfilename]` I will be able to load the file mentioned. Typically this will be used with new commands so don\'t worry about using this command.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)
   
    @commands.command(pass_context=True)
    async def hlol(self, ctx):
        embed = discord.Embed(
            title='__lol__',
            description='I\'ll just send a message saying lol',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hlove(self, ctx):
        embed = discord.Embed(
            title='__love__',
            description='You can tag a user for this command, but it\'s not mandatory. If a user is tagged then I\'ll mention them and tell them how much you *love* them. If a user isn\'t tagged then I\'ll just direct the *love* to everyone in the server (without an \'everyone\' mention).',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hmotivate(self, ctx):
        embed = discord.Embed(
            title='__motivate__',
            description='I have *a bunch* of quotes and with this command I\'ll send a random one.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hmouse(self, ctx):
        embed = discord.Embed(
            title='__mouse__',
            description='sends a random picture of a mouse',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hmusic(self, ctx):
        embed = discord.Embed(
            title='__music__',
            description='After joining a voice channel, if I\'m not in one already, I\'ll hop in with you.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hname(self, ctx):
        embed = discord.Embed(
            title='__name__',
            description='If you don\'t tag a user with this command I\'ll tag you instead. I can generate random names with this command.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hno(self, ctx):
        embed = discord.Embed(
            title='__no__',
            description='You can tag a user for this command, but it\'s not mandatory. I\'ll say \'no u\' to whoever I\'m directed to.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hoof(self, ctx):
        embed = discord.Embed(
            title='__oof__',
            description='I\'ll just respond with different oof messages',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hPatchNotes(self, ctx):
        embed = discord.Embed(
            title='__PatchNotes__',
            description='This is a command that will show you my development through each stage. Look how big I\'ve gotten!',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hpause(self, ctx):
        embed = discord.Embed(
            title='__pause__',
            description='If there\'s a song playing then I\'ll pause it and you can resume it later.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_contex=True)
    async def hpatrol(self, ctx):
        embed = discord.Embed(
            title='__patrol__',
            description='I\'ll mention someone who is trying to get pussy',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_contex=True)
    async def hplay(self, ctx):
        embed = discord.Embed(
            title='__play__',
            description='I\'ll search for music by using whatever you provide after the command (i.e. `-play mr brightside`) or I can play music from a provided youtube link (i.e. -play https://www.youtube.com/watch?v=ccBDu4ZARIo). Also, if I\'m not in a voice channel already I\'ll join the one you\'re in and play what you request.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hplaying(self, ctx):
        embed = discord.Embed(
            title='__playing__',
            description='If a song is playing then this command will give you the title, artist, and song length.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hreload(self, ctx):
        embed = discord.Embed(
            title='__reload__',
            description='This is a really important function. This command will reload a command in order to get it to reboot. To use it type `-reload [command file name]`. I\'ll add a list of my command file names here so if you need to reboot one you\'ll know what it\'s called. **Do not reload this command, it will not be able to boot again.** \n-annoy\n-basic_replies\n-games\n-help\n-maintenance\n-misc\n-music\n-patch_notes\n-pics\nThis command will be used  to perform soft updates on commands in order to avoid shutting me down.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hresume(self, ctx):
        embed = discord.Embed(
            title='__resume__',
            description='If there\'s a paused song then I\'ll start playing it again from where it was paused.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hrip(self, ctx):
        embed = discord.Embed(
            title='__rip__',
            description='Tagging someone with this has no affect. I\'ll send a random \'rip\' message.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hroll(self, ctx):
        embed = discord.Embed(
            title='__roll__',
            description='To use this command enter `-roll[number]d[number]` for the roll; the first number will be the amount of times the dice is rolled and the second number is how many sides the dice will have.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)
    
    @commands.command(pass_context=True)
    async def hrps(self, ctx):
        embed = discord.Embed(
            title='__rps__',
            description='Follow the command with rock, paper, or scissors and we\'ll see who wins',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hshowerthoughts(self, ctx):
        embed = discord.Embed(
            title='__showerthoughts__',
            description='I\'ll send a random shower thought',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hskip(self, ctx):
        embed = discord.Embed(
            title='__skip__',
            description='If a song is playing then this command will start a vote to skip it. Two votes are required to skip it, but if the person who requested it uses this command then I\'ll skip it automatically.',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hslots(self, ctx):
        embed = discord.Embed(
            title='__slots__',
            description='This is a rudimentary slot machine thing. 2 in a row means you win, 3 in a row is a jackpot. There will be more to add to this function so look out for it!',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def htmyk(self, ctx):
        embed = discord.Embed(
            title='__tmyk__',
            description='This command will send a gif of the \'the more you know\' thing',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def htroubleshoot(self, ctx):
        embed = discord.Embed(
            title='__troubleshoot__',
            description='use this command to send a querie to im.ri0t, keep in mind that this command sends the querie asker\'s discord ID and add number (user#0123)',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_contex=True)
    async def huwu(self, ctx):
        embed = discord.Embed(
            title='__uwu__',
            description='I\'ll send uwu ~~there\'s a chance I won\'t though~~',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def hvolume(self, ctx):
        embed = discord.Embed(
            title='__volume__',
            description='If a song is playing this command will allow you to change my personal volume setting for the currently playing song (my default volume is 15%). My minimum is 0% and my max should be kept around 100% for audio quality\'s sake ~~my volume can go up to 200% but you didn\'t hear that from me~~',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_contex=True)
    async def hykn(self, ctx):
        embed = discord.Embed(
            title='__ykn__',
            description='This command will send a png that\'s a remake of the \'the more you know\' gif and says \'you know nothing\'',
            color=0xffffff)
        embed.set_author(name='ri0t-bot', icon_url='https://cdn.discordapp.com/avatars/422901925034459147/e5f233e23ffce4b2fa1b03dd751663e4.png')
        await self.bot.send_message(ctx.message.author, embed=embed)

def setup(bot):
    'cog setup'
    bot.add_cog(Help(bot))
    print('help commands ready')
