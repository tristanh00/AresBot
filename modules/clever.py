import discord
from cleverbot import Cleverbot
cleverbot = Cleverbot('HubbleBot')

class Clever:

    def __init__(self, client):
        self.client = client

    async def ask(self, message):
        new = message.content.replace('<@{}>'.format(self.client.user.id), '')

        answer = cleverbot.ask(new)
        await self.client.send_message(message.channel, answer)
