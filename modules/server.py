import discord
import arrow
import collections

class Server:

    def __init__(self, client):
        self.client = client

    def getRoles(self, roles_objects):
        roles = dict()

        for role in roles_objects:
            roles[role.position] = role.name
        final_roles = []

        d = collections.OrderedDict(sorted(roles.items(), reverse=True))
        for k, v in d.items():
            final_roles.append(v)

        final_roles.remove('@everyone')
        return(', '.join(final_roles))

    def getChannels(self, channels):
        text = 0
        voice = 0
        for channel in channels:
            if channel.type == 4:
                continue
            if channel.type == channel.type.text:
                text += 1
            elif channel.type == channel.type.voice:
                voice += 1
            else:
                continue
        return str(text) + ' text / ' + str(voice) + ' voice'


    async def info(self, message):
        server = message.author.server

        time = arrow.get(server.created_at)
        ago = time.humanize()

        embed = discord.Embed(description='', colour=0x8d378f)
        embed.set_author(name=server.name, icon_url=server.icon_url)
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name='ID', value=server.id, inline=1)
        embed.add_field(name='Server Region', value=str(server.region), inline=1)
        embed.add_field(name='Members', value=str(server.member_count), inline=1)
        embed.add_field(name='Channels', value=self.getChannels(server.channels), inline=1)
        embed.add_field(name='Owner', value=server.owner.name, inline=1)
        embed.add_field(name='Roles', value=self.getRoles(server.roles), inline=0)

        embed.set_footer(text='Created ' + ago + ' | ' + time.format('dddd, MMM Do, YYYY {} h:mm A').format('at'))

        await self.client.send_message(message.channel, embed=embed)
        await self.client.delete_message(message)
