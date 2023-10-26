from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('message/', consumers.AsyncClass.as_asgi()),
]
