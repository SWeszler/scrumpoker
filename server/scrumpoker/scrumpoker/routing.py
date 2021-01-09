from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from poker.consumers import GameConsumer
from django.core.asgi import get_asgi_application


websocket_urlpatterns = [
    path('ws/pol-data/', GameConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    )
})