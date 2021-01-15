from channels.generic.websocket import AsyncWebsocketConsumer
import json


class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'poker',
            self.channel_name
        )
        await self.accept()
        await self.send(json.dumps({'message': "connected!"}))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'poker',
            self.channel_name
        )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        await self.channel_layer.group_send(
            'poker',
            {
                'type': 'chat_message',
                'message': message
            }
        )


    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
