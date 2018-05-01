import discord
import arrow

class Quote:

    def __init__(self, client):
        self.client = client

    async def find(self, message):
        saved = message
        await self.client.delete_message(message)

        async for log in self.client.logs_from(saved.channel, limit=200):
            split = saved.content.split(' ')
            lowered = log.content.lower()

            try:
                if lowered.find(split[1].lower()) != -1:
                    time = arrow.get(log.timestamp)
                    embed = discord.Embed(description=log.content, colour=0x8d378f)
                    embed.set_author(name=log.author.name + ' - ' + time.format('dddd, MMM Do, YYYY {} h:mm A').format('at'), icon_url=log.author.avatar_url)

                    await self.client.send_message(saved.channel, embed=embed)
                    break
            except IndexError:
                await self.client.send_message(saved.channel, 'No message found.')
                break
