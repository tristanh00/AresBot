import discord

class Help:

    def __init__(self, client):
        self.client = client


    async def help(self, message, prefix):
        owner = await self.client.get_user_info('85785887622836224')
        embed =  discord.Embed(description='**Help** - List of Commands', colour=0x8d378f)

        embed.add_field(name=prefix + 'userinfo', value='Get some informations about the requested user.\n\nalias: *' + prefix + 'ui*', inline=1)
        embed.add_field(name=prefix + 'serverinfo', value='Get some informations about the current server.\n\nalias: *' + prefix + 'si*', inline=1)
        embed.add_field(name=prefix + 'fake', value='Fake quote.\n\nalias: *' + prefix + 'fq*', inline=1)
        embed.add_field(name=prefix + 'quote', value='Quote a message with a specific keyword\n\nalias: *' + prefix + 'q*', inline=1)
        embed.set_footer(text='Bot made by tristancode', icon_url=owner.avatar_url)


        await self.client.send_message(message.channel, embed=embed)
        await self.client.delete_message(message)
