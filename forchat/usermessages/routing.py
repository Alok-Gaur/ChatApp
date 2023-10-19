from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ac/message', consumers.AsyncClass.as_asgi()),
]
