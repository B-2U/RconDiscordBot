import os
import json
import discord
from discord.ext import commands
from mcrcon import MCRcon

if os.path.exists('rcon_bot_config.json'):
    with open('rcon_bot_config.json') as file:
        config = json.load(file)
else:
    open('rcon_bot_config.json', 'w')
    with open('rcon_bot_config.json', 'w') as file:
        default = {'TOKEN': '',
                   'PREFIX': '--',
                   'IP': '127.0.0.1',
                   'rcon_pw': '',
                   'rcon_port': 25500,
                   'query_port': 25500,
                   'server_path': '.\start.bat',
                   'console_channel': []
                   }
        json.dump(default, file, indent=4)
    print("No config detected. Please edit rcon_bot_config.json and run this program again.")
    exit()

PREFIX = config['PREFIX']
ip = config['IP']
rcon_pw = config['rcon_pw']
rcon_port = config['rcon_port']

bot = commands.Bot(PREFIX)


@ bot.event
async def on_ready():
    print(f'{bot.user} --{__file__}')
    try:
        os.system(f'start {config["server_path"]}')
    except:
        pass


@ bot.event
async def on_message(msg):
    if msg.channel.id in config['console_channel'] and msg.content.startswith(PREFIX) and not msg.author.bot:
        if msg.content == (f'{PREFIX}start'):
            try:
                MCRcon(ip, rcon_pw, port=rcon_port)
                await msg.channel.send('Server is already running!')
            except:
                os.system(f'start {config["server_path"]}')
        else:
            prefix_msg = msg.content.replace(PREFIX, '/')
            with MCRcon(ip, rcon_pw, port=rcon_port) as mcr:
                resp = mcr.command(prefix_msg)

            embed = discord.Embed(
                title=resp, description=prefix_msg, color=0xffff00)
            embed.set_footer(text=msg.author)
            await msg.channel.send(embed=embed)


bot.run(config['TOKEN'])
