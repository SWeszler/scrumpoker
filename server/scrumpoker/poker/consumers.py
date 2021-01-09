from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
import json
from random import randint

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            await self.send(json.dumps({'message': randint(1, 1000)}))
            await sleep(1)

    async def disconnect(self):
        print('Game Consumer disconnected.')

    async def receive(self, text_data):
        print(text_data)
        await self.send(json.dumps({'message': 'Thanks!'}))
