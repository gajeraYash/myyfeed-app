"""
ASGI config for CS490 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, get_default_application
from channels.layers import get_channel_layer
from channels.security.websocket import AllowedHostsOriginValidator
import app.routing
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CS490.settings")
django.setup()
application = get_default_application()
channel_layer = get_channel_layer()

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                app.routing.websocket_urlpatterns
            )
        )
    ),
})
