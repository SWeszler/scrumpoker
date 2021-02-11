from channels.generic.websocket import AsyncWebsocketConsumer
from poker.models import Player
from channels.db import database_sync_to_async
import json


class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'room',
            self.channel_name
        )
        await self.accept()
        await self.add_player(self.scope['user'])
        await self.channel_layer.group_send( 'room', { 'type': 'data_handler' })


    async def disconnect(self, close_code):
        # await self.remove_player(self.scope['user'])
        await self.channel_layer.group_send( 'room', { 'type': 'data_handler' })
        await self.channel_layer.group_discard( 'room', self.channel_name )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        await self.add_player(text_data_json['player'])
        await self.channel_layer.group_send( 'room', { 'type': 'data_handler' })


    async def data_handler(self, event):
        players = await self.get_players()
        await self.send(text_data=json.dumps({
            'players': players
        }))


    @database_sync_to_async
    def add_player(self, name):
        return Player.objects.get_or_create(name=name)


    @database_sync_to_async
    def remove_player(self, name):
        return Player.objects.filter(name=name).delete()


    @database_sync_to_async
    def get_players(self):
        return [player.name for player in Player.objects.all()]


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'game',
            self.channel_name
        )
        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'game',
            self.channel_name
        )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        await self.channel_layer.group_send(
            'game',
            {
                'type': 'data_handler',
                'vote': text_data_json['vote'],
                'player': text_data_json['player']
            }
        )


    async def data_handler(self, event):
        await self.send(text_data=json.dumps({
            'vote': event['vote'],
            'player': event['player']
        }))
