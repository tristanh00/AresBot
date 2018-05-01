import discord
import asyncio
import collections

from modules.quote import Quote
from modules.user import User
from modules.help import Help
from modules.fakequote import Fakequote
from modules.server import Server

client = discord.Client()
quote = Quote(client)
user = User(client)
help = Help(client)
server = Server(client)
fq = Fakequote(client)

prefix = ':'
version = 'v1.0.7'
voice = None
player = None

@client.event
async def on_ready():

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Servers')
    for server in client.servers:
        print('-------------------------------------------')
        print('Name          : ' + server.name)
        print('Total Members : ' + str(server.member_count))
        print('Server Owner  : ' + server.owner.name)

    await client.change_presence(game=discord.Game(name=prefix + 'help - ' + version, type=1))

    # picture = open("new.jpg", "rb")
    # picture_bits = picture.read()
    # picture.close()
    # await client.edit_profile(avatar=picture_bits)
    # await client.edit_profile(username="AresBot")


@client.event
async def on_message(message):
    global voice
    global player
    if message.content.startswith('<@{}>'.format(client.user.id)):
        await client.send_message(message.channel, '{} Wsh?'.format(message.author.mention))

    if message.content.startswith(prefix + 'help'):
        await help.help(message, prefix)

    if message.content.startswith(prefix + 'serverinfo') or message.content.startswith(prefix + 'si'):
        await server.info(message)

    if message.content.startswith(prefix + 'stab'):
        usr = message.mentions
        if(len(usr) < 1):
            await client.send_message(message.channel, '{} just stabbed himself... :knife:'.format(message.author.mention))
        else:
            await client.send_message(message.channel, '{} just stabbed {} :knife::scream:'.format(message.author.mention, usr[0].mention))
            f = open('die.txt','r')
            string = ""
            while 1:
                line = f.readline()
                if not line:
                    break
                string += line
            f.close()

            await client.send_message(usr[0], string)
        await client.delete_message(message)

    if message.content.startswith(prefix + 'quote') or message.content.startswith(prefix + 'q'):
        await quote.find(message)

    if message.content.startswith(prefix + 'fake') or message.content.startswith(prefix + 'fq'):
        await fq.quote(message)

    if message.content.startswith(prefix + 'userinfo') or message.content.startswith(prefix + 'ui'):
        await user.info(message)

client.run('')
