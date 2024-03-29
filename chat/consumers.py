from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Chat, ChatRoom
from accounts.models import Profile

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = text_data_json['user']
        room_id = text_data_json['room']
        user = Profile.objects.get(pk = user_id)
        room = ChatRoom.objects.get(pk = room_id)
        chat = Chat(
            sender = user,
            text = message,
            room = room,
        )
        chat.save()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            { 'type': 'chat_message', 'message': message, 'user_name': user.user_name, 'user_room_num': user.room_number, }
        )
        
    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        user_name = event['user_name']
        user_room_num = event['user_room_num']
        # Send message to WebSocket
        self.send(text_data=json.dumps({'message': message, 'user_name': user_name, 'user_room_num': user_room_num, }))