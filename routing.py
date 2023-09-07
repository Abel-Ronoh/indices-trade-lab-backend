# routing.py

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/notifications/$", consumers.NotificationConsumer.as_asgi()),
]
# project_root/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import your_app.routing  # Import your app's WebSocket routing

application = ProtocolTypeRouter(
    {
        # ...other protocols...
        "websocket": AuthMiddlewareStack(
            URLRouter(
                your_app.routing.websocket_urlpatterns
            )
        ),
    }
)
## replace your_app with the actuall name of your app
# routing.py

