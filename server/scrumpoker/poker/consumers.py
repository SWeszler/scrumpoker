from channels.generic.websocket import AsyncWebsocketConsumer
from poker.models import Player
from channels.db import database_sync_to_async
import json


class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "room",
            self.channel_name
        )
        await self.accept()
        await self.get_or_create_player(self.scope["user"])
        await self.channel_layer.group_send( "room", { "type": "data_handler" })


    async def disconnect(self, close_code):
        await self.deactivate_player(self.scope["user"])
        await self.channel_layer.group_send( "room", { "type": "data_handler" })
        await self.channel_layer.group_discard( "room", self.channel_name )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json.get("restart"):
            await self.restart_game()
        else:
            await self.player_vote(name=self.scope["user"], vote=text_data_json["vote"])
        await self.channel_layer.group_send( "room", { "type": "data_handler" })


    async def data_handler(self, event):
        players = await self.get_players()
        await self.send(text_data=json.dumps({
            "players": players
        }))


    @database_sync_to_async
    def get_or_create_player(self, name):
        player, _ = Player.objects.get_or_create(name=name)
        player.active = True
        player.save(update_fields=["active"])
        
        return player


    @database_sync_to_async
    def player_vote(self, name, vote):
        player = Player.objects.filter(name=name).first()
        if player:
            if not player.voted:
                player.vote = int(vote)
            player.voted = True
            player.save(update_fields=["vote", "voted"])



    @database_sync_to_async
    def deactivate_player(self, name):
        player = Player.objects.filter(name=name).first()
        if player:
            player.active = False
            player.save(update_fields=["active"])


    @database_sync_to_async
    def get_players(self):
        players = []
        for player in Player.objects.all():
            if not player.active:
                continue
            players.append({
                "name": player.name,
                "vote": player.vote,
                "voted": player.voted
            })
        return players


    @database_sync_to_async
    def restart_game(self):
        players = []
        for player in Player.objects.all():
            player.voted = False
            player.save(update_fields=["voted"])
        return players


