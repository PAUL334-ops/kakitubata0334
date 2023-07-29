import discord
import googleapiclient
from googleapiclient.discovery import build
import os
import random
from discord import Intents, Client, Interaction
from discord.app_commands import CommandTree
from discord.ext import tasks
#トークン
TOKEN = "MTEzNDQ0NTMyMDQ1ODIxNTQ5NQ.G04pmY.OvQrutkTKcbziri30Aj-APGB4mge_fcMF-nJME"
#起動時に必要なオブジェクト
client = discord.Client()
#起動時の動作
@client.event

async def onmessage(message):

    if message.auther.bot:
        return
    if message.content == "/ハコニワリリィ":
        await message.channel.send("https://www.youtube.com/@HaKoniwalily")

title1 = 0
@tasks.loop(seconds=15)
async def send_message_hanon():
 API_KEY = "AIzaSyB_Glb5ap_MjnsGNmqQ-T5qw_U2TWRYO_4"
 API_VER = "v3"
 youtube = build('youtube',API_VER,developerKey=API_KEY)
def getChannelPlaylistId(channel_id):
  channel = youtube.channels().list(part='snippet,contentDetails', id=channel_id).execute()
  item = channel['items'][0]
  playlist_id = item['contentDetails']['relatedPlaylists']['uploads']
  return playlist_id
def getvideoIds(playlist_id,page_token):
  items_info = youtube.playlistItems().list(part='contentDetails',playlistId = playlist_id,maxResults=10,pageToken=page_token).execute()
  video_ids = list(map(lambda item: item['contentDetails']['videoId'],items_info['items']))
  return video_ids

def getVideos(video_ids):
  videos = []
  for index, video_id in enumerate(video_ids):
    video_info = youtube.videos().list(part='snippet,statistics',id=video_id).execute()
    videos.extend(video_info['items'])
    return videos
  
channel_id = 'UCJB1hgmiAD4ysg0Ao7uS8Rw'
playlist_id = getChannelPlaylistId(channel_id)
videos_ids = getvideoIds(playlist_id,None)
videos = getVideos(videos_ids)



videos = getVideos(videos_ids)

videos
for video in videos :
  title = video['snippet']['title']

if title == title1 :
   pass
else:
   print(video['snippet']['title'], ',', 'https://youtube.com/watch?v=' + video['id'])
title1 = title
 
