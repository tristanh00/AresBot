import discord
import requests
from json import loads, dumps
import base64
import urllib.request

class Fakequote:

    def __init__(self, client):
        self.client = client

    async def quote(self, message):
        if len(message.mentions) >= 1:
            user = message.mentions[0]
        else:
            user = message.author

        url = 'https://discordapp.com/api/channels/{}/webhooks'.format(message.channel.id)
        headers = {'Content-type': 'application/json', 'Authorization': 'Bot'}

        #First we create it!
        image = urllib.request.Request(user.avatar_url)

        image.add_header('Authorization', 'Bot')
        image.add_header('User-Agent', 'DiscordBot')
        bytes = urllib.request.urlopen(image)

        encoded = base64.b64encode(bytes.read()).decode('utf-8')

        data = {'name': user.name, 'avatar': "data:image/jpeg;base64," + str(encoded)}
        create = requests.post(url, data=dumps(data), headers=headers)

        out = create.json()

        #Post the webhook
        webhook_url_token = 'https://discordapp.com/api/webhooks/{}/{}'.format(out['id'], out['token'])

        data2 = {'name': user.name, 'content': message.content.replace(':fake', '')}
        send = requests.post(webhook_url_token, data=dumps(data2), headers=headers)

        #Delete the webhook
        delete = requests.delete(webhook_url_token,headers=headers)
