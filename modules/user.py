import discord
import arrow
import collections

class User:

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

    async def info(self, message):
        if len(message.mentions) >= 1:
            user = message.mentions[0]
        else:
            user = message.author
        time = arrow.get(user.joined_at)
        ago = time.humanize()
        embed = discord.Embed(description='', colour=0x8d378f)
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name='ID', value=user.id, inline=1)
        embed.add_field(name='Discriminator', value=user.discriminator, inline=1)
        embed.add_field(name='Status', value="do not disturb" if user.status == user.status.dnd else str(user.status), inline=1)
        if user.game != None:
            embed.add_field(name='Game', value=user.game.name, inline=1)
        embed.add_field(name='Top Role', value='None' if user.top_role.name == '@everyone' else user.top_role.name, inline=1)
        embed.add_field(name='Joined', value=ago + " | " + time.format('dddd, MMM Do, YYYY {} h:mm A').format('at'), inline=1)
        embed.add_field(name='Roles', value=self.getRoles(user.roles), inline=0)
        embed.set_footer(text='User information requested by ' + message.author.name, icon_url=message.author.avatar_url)

        await self.client.send_message(message.channel, embed=embed)
        await self.client.delete_message(message)
