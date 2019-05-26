import discord
import asyncio

client = discord.Client()

time = {'ice':60*60*4, 'eno':60*60*4, 'col':60*60*5}
name = {'ice':'Ice', 'eno':'Eno', 'col':'Col'}

@client.event
async def on_ready():
    print('Discord bot online as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        task, dep, px = message.content[1:].split(' ')
        if dep == 'depleted':
            await wait_and_send(message.channel, task, px)
        
async def wait_and_send(channel, task, px):
    await channel.send(name[task] + ' marked as depleted for ' + str(px))
    await asyncio.sleep(time[task])
    await channel.send('@here ' + name[task] + ' for ' + str(px) + ' has respawned')

client.run('INSERT BOT TOKEN')

