from app.models import ChatMessage, Thread
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.exceptions import StopConsumer


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, message):
        print("connected", message)
        other_user = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
        print(other_user, me)
        thread_obj = await self.get_thread(me, other_user)
        self.thread_obj = thread_obj
        chat_room = f"chat_thread__{thread_obj.id}"
        self.chat_room = chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, message):
        print("received", message)
        msg_receive = message.get('text', None)
        if msg_receive is not None:
            dict_data = json.loads(msg_receive)
            msg = dict_data.get('message')
            user = self.scope['user']
            response = {
                'message': msg,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
            print(response)
            await self.msg_create(user, msg)
            # broadcast message event
            await self.channel_layer.group_send(
                self.chat_room,
                {
                    "type": "chat_message_event",
                    "text": json.dumps(response)
                }
            )

    async def chat_message_event(self, event):
        # sending the message event
        print('message', event)
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, message):
        print("disconnected", message)
        await self.channel_layer.group_discard(
            self.chat_room,
            self.channel_name
        )
        raise StopConsumer()

    @database_sync_to_async
    def get_thread(self, user, other_username):
        return Thread.objects.get_or_new(user, other_username)[0]

    @database_sync_to_async
    def msg_create(self, user, message):
        thread_obj = self.thread_obj
        return ChatMessage.objects.create(thread=thread_obj, user=user, message=message)
