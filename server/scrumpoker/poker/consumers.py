from channels.generic.websocket import AsyncWebsocketConsumer


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self, event):
        await self.connect()
        print("connected", event)

    async def disconnect(self, close_code):
        await self.disconnect()

    async def receive(self, text_data):
        print('>>>>', text_data)
