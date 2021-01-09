from channels.generic.websocket import AsyncWebsocketConsumer
import json


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(json.dumps({'message': "hello!"}))

    async def disconnect(self):
        print('Game Consumer disconnected.')

    async def receive(self, text_data):
        print(text_data)
        await self.send(json.dumps({'message': text_data}))
