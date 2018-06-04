# from django.conf.urls import url

# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack

# from myapp import consumers

# application = ProtocolTypeRouter({

#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             url(r"^front(end)/$", consumers.AsyncChatConsumer),
#         ])
#     ),

# })


# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})