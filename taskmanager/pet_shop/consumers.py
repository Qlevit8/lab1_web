
from channels.generic.websocket import AsyncWebsocketConsumer
import json

active_users = []


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'notification'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        user = self.scope["user"]
        if user.is_authenticated:
            user_info = {
                "name": user.name + ' ' + user.surname,
                "email": user.email,
                "channel_name": self.channel_name
            }
        else:
            user_info = {
                "name": "Anonymous",
                "email": "Unknown",
                "channel_name": self.channel_name
            }

        self.user_info = user_info

        active_users.append(user_info)
        #active_users.append(name)
        await self.send_active_users()

    async def disconnect(self, code):
        if self.user_info in active_users:
            active_users.remove(self.user_info)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        await self.send_active_users()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        event = {
            'type': 'send_message',
            'message': message
        }
        await self.channel_layer.group_send(self.group_name, event)

    async def send_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message, 'tag': 'pet_purchase'}))

    async def send_active_users(self):
        active_users_list = {
            'type': 'active_users',
            'users': active_users
        }
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'broadcast_active_users',
                'active_users_list': active_users_list
            }
        )

    async def broadcast_active_users(self, event):
        active_users_list = event['active_users_list']
        await self.send(text_data=json.dumps(active_users_list))