from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.urls import path, re_path
from chat.consumers import ChatConsumer
from tailf.consumers import TailfConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/', ChatConsumer),
            re_path(r'^ws/tailf/(?P<id>\d+)/$', TailfConsumer),
        ])
    )
})
