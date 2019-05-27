import asyncio
import time
import datetime

import discord


client = discord.Client()
id_ctr = 1
duration = {'ice':60*60*4, 'eno':60*60*4, 'col':60*60*5}
name = {'ice':'Ice', 'eno':'Eno', 'col':'Col'}
timer_list = []

help_message = \
"""
!ice depleted Region 
!eno depleted Region 
!col depleted Region
!list
!status {ice, eno, col}
!status {ice, eno, col} Region
!delete id
"""

@client.event
async def on_ready():
    print('Discord bot online as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        com = message.content[1:].split(' ')[0]
        if com in ['ice', 'eno', 'col']:
            task, dep, px = message.content[1:].split(' ')
            if dep == 'depleted' and task in name.keys():
                timer_list.append(create_timer(message.channel, task, px))
        
        if com == 'list':
            com = message.content[1:].split(' ')
            stat = get_status_string(timer_list)
            await message.channel.send(stat)
            
        if com == 'status':
            if len(message.content[1:].split(' ')) == 2:
                com, task = message.content[1:].split(' ')
                stat = get_status(task)
                await message.channel.send(stat)

            if len(message.content[1:].split(' ')) == 3:
                com, task, px = message.content[1:].split(' ')
                stat = get_status_reg(task, px)
                await message.channel.send(stat)
            
        if com == 'delete':
            com, id = message.content[1:].split(' ')
            delete_id(id)
            stat = get_status_string(timer_list)
            await message.channel.send(stat)
            
        if com == 'help':
            await message.channel.send(help_message)

def get_status_reg(task, px):
    timer_sublist = []
    for item in timer_list:
        if item['class'] == task and item['px'] == px:
            timer_sublist.append(item)
    
    return get_status_string(timer_sublist)

def get_status(task):
    timer_sublist = []
    for item in timer_list:
        if item['class'] == task:
            timer_sublist.append(item)
    
    return get_status_string(timer_sublist)

def get_status_string(timer_sublist):
    lines = []
    for i,item in enumerate(timer_sublist, 1):
        line =  str(item['id']) + '- ' \
                + item['class'] + ' ' \
                + item['px'] + '- '\
                + format_time(item['finish'] - time.time())
        lines.append(line)
    if not(len(lines)):
        return 'No active countdowns'
    else:
        return 'Active timers: \n' + '\n'.join(lines)
    
def format_time(sec):
    return str(datetime.timedelta(seconds=int(sec)))

async def start_timer(channel, task, px):
    await channel.send(name[task] + ' marked as depleted for ' + str(px))
    await asyncio.sleep(duration[task])
    update_timer()
    await channel.send('@here ' + name[task] + ' for ' + str(px) + ' has respawned')
  
def delete_id(id):
    global timer_list
    timer_list = [t for t in timer_list if (t['id'] != int(id))]
    
def update_timer():
    global timer_list
    timer_list = [t for t in timer_list if (t['finish'] - time.time())>0]
    
def create_timer(channel, task, px):
    global id_ctr
    timer = {'task': asyncio.ensure_future(start_timer(channel, task, px)), 
             'class': task, 
             'px': px, 
             'finish': time.time() + duration[task],
             'id': id_ctr}
    id_ctr = (id_ctr + 1) % 1000
    return timer


client.run('Token goes here ')
