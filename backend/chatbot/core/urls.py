# yourapp/urls.py

from django.urls import path
from .views import InitiateSession, Chat

urlpatterns = [
    path('initiate_session/', InitiateSession.as_view(), name='initiate_session'),
    path('chat/', Chat.as_view(), name='chat'),
]
