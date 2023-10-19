from channels.consumer import AsyncConsumer

# Here making Async Class


class AsyncClass(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connect...", event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("Websocket Received...", event)

    async def websocket_disconnect(self, event):
        print('Websocket Disconnected....', event)
