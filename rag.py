import pickle
import os

embeddings_model_name = "intfloat/multilingual-e5-base"
embeddings_path = "./path_to_model/intfloat/multilingual-e5-base"
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

with open('retriever.pkl','rb') as f:
    retriever = pickle.load(f)

from helpers import LLM

llm = LLM()

# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください

# 接続に必要なオブジェクトを生成
intents=discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)
CHANNEL_IDs = [1248267523187802113,1224164970653290598] 

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    #for CHANNEL_ID in CHANNEL_IDs:
        #await client.get_channel(CHANNEL_ID).send('ログインしました')

# 返信する非同期関数を定義
async def reply(message):
    reply = llm.chat(message.content, retriever, show=False, source=False)
    reply = reply.replace("<@1304329870632947732>",'')
    print(reply)
    await message.channel.send(reply) # 返信メッセージを送信

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        print(message.content)
        await reply(message) # 返信する非同期関数を実行


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)