import discord
from discord import member
from discord import embeds
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.flags import Intents
from discord import FFmpegPCMAudio
from mutagen.mp4 import MP4
import pytube
from pytube import YouTube
from pytube import Playlist
import os
import time

client = discord.Client()
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix= 'dave ',intents = intents)



@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    

@client.command()
async def harrass(ctx,message):
    voiceChannel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voiceChannel.connect()
    else:
        await ctx.voice_client.move_to(voiceChannel)
   
    name = message
    
    path = "C:\\Users\\Dulguun\\Desktop\\DuuuluuBot9000\\"+name+".mp3"
    await ctx.send(path)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\ffmpeg.exe",source = path))

    
    
@client.command()
async def playlist(ctx,url : str):
    voiceChannel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voiceChannel.connect()
    else:
        await ctx.voice_client.move_to(voiceChannel)
    
    # try:
    #     os.remove("C:\\Users\\Dulguun\\Desktop\\DuuuluuBot9000\\music\\song.mp3")
        
    # finally:
    #     print("failed")
    path = 'C:\\Users\\Dulguun\\Desktop\\DuuuluuBot9000\\playlist\\'
    
    p = Playlist(url)
    for file in os.listdir(path):
        p4 = path + file
        os.remove(p4)
    for vid in p.videos:
        video = vid.streams.filter(only_audio=True).first()
        song = video.download(output_path=path)
    
    t1 = 1
    names = ["123"]
    names.pop(0)
    for file in os.listdir(path)
        source = path + file
        names.append(file)
        t2 = str(t1)
        rename = path + "song"+t2+".mp3"
        os.rename(source,rename)
        t1 = t1 + 1
    # for file_name in os.listdir(path):
    #     source = path + file_name
    #     await ctx.send("Playing "+ file_name)
    #     rename = path + "song.mp3"
    #     os.rename(source,rename)


    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    number = 0
    await ctx.send(voice.is_playing())
    for file in os.listdir(path):
        s1 = path + file
        voice.play(discord.FFmpegPCMAudio(s1))
        audio = MP4(s1)
        name1 = names[number].replace(".mp4","")
        await ctx.send("Playing "+name1)
        time.sleep(audio.info.length)
        number = number + 1               
@client.command()
async def yt(ctx,url : str):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        
    voiceChannel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voiceChannel.connect()
    else:
        await ctx.voice_client.move_to(voiceChannel)
        
    
    try:
        os.remove("C:\\Users\\Dulguun\\Desktop\\DuuuluuBot9000\\music\\song.mp3")
        
    finally:
        print("failed")
    path = 'C:\\Users\\Dulguun\\Desktop\\DuuuluuBot9000\\music\\'
    
    yut = YouTube(url)
    video = yut.streams.filter(only_audio=True).first()
    song = video.download(output_path=path)
    for file_name in os.listdir(path):
        source = path + file_name
        await ctx.send("Playing "+ file_name)
        rename = path + "song.mp3"
        os.rename(source,rename)


    
    voice.play(discord.FFmpegPCMAudio("C:\\Users\\Dulguun\\Desktop\\DuuuluuBot9000\\music\\song.mp3"))
    

    
@client.command()
async def zl(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_connected:
        await voice.disconnect()
        await ctx.send("ok bye")
    else:
        await ctx.send("not in vc dumbass")



@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("pausin")
    else:
        await ctx.send("Playin fk all m8")



@client.command()
async def go(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send("resumin")
    else:
        await ctx.send("Nothin paused??")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    await ctx.send("stoppun")
    voice.stop()



@client.command()
async def fuck(ctx):
    await ctx.send("no fuck u")


@client.command()
async def msg(ctx, user:discord.Member,* ,message = None):
    message = "Fuck u lmao"
    embed = discord.Embed(title = message)
    await user.send(embed = embed)
client.run('ODk4NDc3Nzk1MzA1NDY3OTA0.YWkypw.desCPIrBiWTTy9yX9QnleE5knug')
