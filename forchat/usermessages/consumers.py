from channels.consumer import AsyncConsumer
import json
from channels.db import database_sync_to_async
from channels.auth import get_user_model
from .models import Thread, ChatMessage
from django.db.models import Q
from datetime import datetime
# Here making Async Class

User = get_user_model()


class AsyncClass(AsyncConsumer):
    async def websocket_connect(self, event):
        # print("Websocket Connect...", event)
        user = self.scope['user']

        # This is chatroom of user who sent the message.
        # print('the user currently logged in is ', user.id)
        chat_room = f'user_chatroom_{user.id}'
        self.chat_room = chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        # print("Websocket Received...", event)
        recieved_data = json.loads(event['text'])
        if recieved_data.get("type") == 'message':
            msg = recieved_data.get('message')
            sent_by_id = recieved_data.get('sent_by')
            send_to_id = recieved_data.get('send_to')
            thread_id = recieved_data.get('thread_id')

            if not msg:
                # print('Error :: Empty Message!')
                return False

            sent_by_user = await self.get_user_object(sent_by_id)
            send_to_user = await self.get_user_object(send_to_id)
            thread_obj = await self.get_thread(thread_id)

            await self.create_chat_message(thread_obj, sent_by_user, msg, send_to_user)

            other_user_chat_room = f"user_chatroom_{send_to_id}"
            self_user = self.scope['user']  # this is current logged in user
            response = {
                'message': msg,
                'sent_by': self_user.id,
                'thread_id': thread_id
            }

            await self.channel_layer.group_send(
                other_user_chat_room,
                {
                    'type': 'chat_message',
                    'text': json.dumps(response)
                }
            )

            await self.channel_layer.group_send(
                self.chat_room,
                {
                    'type': 'chat_message',
                    'text': json.dumps(response)
                }
            )
        elif recieved_data.get('type') == 'search':
            data = await self.search_users(recieved_data.get('search'))
            print(recieved_data.get('search'))
            if data:
                await self.send({
                    'type': 'websocket.send',
                    'text': json.dumps({'identity': 'search-user', 'data': data})
                })

    async def websocket_disconnect(self, event):
        # print('Websocket Disconnected....', event)
        pass

    async def chat_message(self, event):
        # print('Chat Message', event)
        await self.send({
            'type': 'websocket.send',
            'text': event['text'],
        })

    @database_sync_to_async
    def get_user_object(self, user_id):
        qs = User.objects.filter(id=user_id)
        if qs.exists():
            obj = qs.first()
        else:
            obj = None
        return obj

    @database_sync_to_async
    def get_thread(self, thread_id):
        qs = Thread.objects.filter(id=thread_id)
        if qs.exists():
            obj = qs.first()
        else:
            obj = None
        return obj

    @database_sync_to_async
    def create_chat_message(self, thread, user, msg, user2):
        ChatMessage.objects.create(
            thread=thread, user=user, message=msg)
        obj = Thread.objects.filter(
            Q(first_person=user) & Q(second_person=user2) | Q(
                first_person=user2) & Q(second_person=user)
        ).update(updated=datetime.now())


# This function search for all the matching user in the database and send to the user


    @database_sync_to_async
    def search_users(self, searched_user):
        users = User.objects.filter(username__icontains=searched_user).values_list(
            'id', 'username').all()
        serialized_user = [
            {'id': id, 'username': username} for id, username in users]
        return serialized_user
