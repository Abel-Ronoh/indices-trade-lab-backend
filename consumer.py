# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Allow only authenticated users to connect
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            await self.accept()

    async def disconnect(self, close_code):
        # Handle disconnecting clients, if needed
        pass

    async def notify_deposit(self, event):
        # Send a deposit notification to the user
        message = event["message"]

        await self.send(json.dumps({"notification_type": "deposit", "message": message}))
