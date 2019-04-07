'''cog: music'''
import asyncio
import re
from datetime import timedelta

import youtube_dl
import urllib.parse
import urllib.request

import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

song_list = []

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

voice = None
player = None

def __init__(self, bot):
    self.bot = bot

class VoiceEntry(): # pylint: disable=too-few-public-methods
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = ' {0.title}'
        try:
            duration = self.player.duration
            if duration:
                fmt = fmt + ' [{0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        except Exception:
            print('no duration identified')
        finally:
            try:
                return fmt.format(self.player, self.requester)
            except Exception as e:
                print(str(e))                

class VoiceState():
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'we\'re listening to ' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()

class Music():
    '''Voice related commands.
    Works in multiple servers at once.'''
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_yturl(self, song):
        #do query
        query_string = urllib.parse.urlencode({"search_query" : song})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        return "http://www.youtube.com/watch?v=" + search_results[0]

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state
        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True, aliases=['MUSIC', 'join', 'JOIN'])
    async def music(self, ctx):
        '''Summons the bot to join your voice channel.'''
        s_ch = ctx.message.author.voice_channel
        global voice
        if s_ch is None:
            await self.bot.say('this isn\'t a voice channel, my guy')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(s_ch)
        else:
            await state.voice.move_to(s_ch)

    @commands.command(pass_context=True, no_pm=True)
    @commands.cooldown(1,5,BucketType.user)
    async def play(self, ctx, *, song):
        '''Plays a song and joins a voice channel if not in one already.
        If there is a song currently in the queue, then it is
        queued until the next song is done playing.
        This command automatically searches as well from YouTube.
        The list of supported sites can be found here:
        https://rg3.github.io/youtube-dl/supportedsites.html'''
        global song_list 
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        s_ch = ctx.message.author.voice_channel
        if s_ch is None:
            await self.bot.say('this isn\'t a voice channel, my guy')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(s_ch)
        else:
            await state.voice.move_to(s_ch)

        await self.bot.say('*searching for them beatsies...*')

        url = self.get_yturl(song)
        try:
            player = await state.voice.create_ytdl_player(url, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'there\'s an error: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            if player.duration > 3600:
                await self.bot.say('that\'s a whole lot of music right there dude, chill')
                return
            player.volume = 0.3
            song_list.append(url)
            entry = VoiceEntry(ctx.message, player)
            await self.bot.say('enqueued ' + str(entry))
            await state.songs.put(entry)

    @commands.command(pass_context=True, no_pm=True)
    async def pause(self, ctx):
        '''Pauses the currently playing song'''
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.pause()

    @commands.command(pass_context=True, no_pm=True, aliases=['vol'])
    async def volume(self, ctx, value: int):
        '''Sets the volume of the currently playing song.'''
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            await self.bot.say('the volume is {:.0%}'.format(player.volume))

    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        '''Resumes the currently played song.'''
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(pass_context=True, no_pm=True)
    async def leave(self, ctx):
        '''Stops playing audio and leaves the voice channel.
        This also clears the queue.'''
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
            await self.bot.say('the queue is cleared, I\'m out yo ')
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        '''Vote to skip a song. The song requester can automatically skip.
        2 skip votes are needed for the song to be skipped.'''
        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            await self.bot.say('there ain\'t no tunes playing')
            return

        voter = ctx.message.author
        if voter == state.current.requester:
            await self.bot.say('the __dork__ who wanted this song skipped it')
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            if total_votes >= 2:
                await self.bot.say('*fuck this song,* ***skip***')
                state.skip()
            else:
                await self.bot.say('we\'re trying to skip this song, we gots [{}/2] votes'.format(total_votes))
        else:
            await self.bot.say('you already voted, dork')

    @commands.command(pass_context=True, no_pm=True)
    async def playing(self, ctx):
        '''Shows info about the currently played song.'''
        state = self.get_voice_state(ctx.message.server)
        if state.current is None:
            await self.bot.say('no songs playing atm')
        else:
            await self.bot.say('we\'re listening to {}'.format(state.current))

    @commands.command(pass_context=True, aliases=['Queue', 'q', 'Q'])
    async def queue(self, ctx):
        '''shows enqueued songs and the duration of all enqueued music'''
        #use markdown in embeds
        global VoiceEntry

        state = self.get_voice_state(ctx.message.server)
        #counter = 1
        queue = state.songs._queue
        q_str = ''
        dur = 0

        for pos, s in enumerate(queue):
            try:
                dur += s.player.duration
            except:
                pass

        q_str += '\nnow playing: {}'.format(state.current.player.title if state.current.player.title else 'unknown song')
        for pos, s in enumerate(queue):
            q_str += '\n{0}: {1}\n'.format(pos+1, s.player.title if s.player.title is not None else 'unknown song')
        q_str += '\ntotal queue time: {}\n'.format(str(timedelta(seconds=dur)))

        await self.bot.say(q_str)

        if not state.is_playing():
            await self.bot.say('nothing\'s queued, dude')
            return

def setup(bot):
    '''cog setup'''
    bot.add_cog(Music(bot))
    print('music commands ready')
