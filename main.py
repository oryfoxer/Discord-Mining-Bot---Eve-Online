import discord
from discord.ext import commands
import asyncio

# Client info
prefix = '!'
client = commands.Bot(command_prefix=prefix)

time = {'ice':60*60*4, 'eno':60*60*4, 'col':60*60*5}
name = {'ice':'Ice', 'eno':'Eno', 'col':'Col'}


@client.event
async def on_ready():
    print('Discord bot online as {0.user}'.format(client))


@client.command()
async def depleted(ctx):
    task = ctx.message.content.split(' ')[1].lower()
    px = ctx.message.content.split(' ')[2]
    await wait_and_send(ctx.message.channel, task, px)


async def wait_and_send(channel, task, px):
    await channel.send(name[task] + ' marked as depleted for ' + str(px))
    await asyncio.sleep(time[task])
    await channel.send('@here ' + name[task] + ' for ' + str(px) + ' has respawned')

client.run('Token goes here')

