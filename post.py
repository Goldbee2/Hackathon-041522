from dis import disco
import discord


TOKEN=""
GUILD_ID=""
CHANNEL_ID = ""

info = open('info.txt')
content = info.readlines()
for line in content:
    line = line.split(' ')
    if(len(line)==0):break
    if(line[0]=="TOKEN"):
        TOKEN = line[1]
    if(line[0]=="GUILD_ID"):
        GUILD_ID = line[1]
    if(line[0]=="CHANNEL_ID"):
        CHANNEL_ID = line[1]








cl = discord.Client()

@cl.event
async def on_ready():
    guild = cl.get_guild(GUILD_ID)
    channel = cl.get_channel(int(CHANNEL_ID))
    my_file = discord.File('content/test.png')
    
    await channel.send('let\'s begin.', file=my_file)
    await cl.close()

    
cl.run(TOKEN)