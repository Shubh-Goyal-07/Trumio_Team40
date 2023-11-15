# yourapp/urls.py

from django.urls import path
from .views import FileUploadView, FileListView, FileDeleteView, InitiateSession, Chat

urlpatterns = [
    path('uploads/', FileUploadView.as_view(), name='upload_file'),
    path('list/', FileListView.as_view(), name='file_list'),
    path('delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),
    path('initiate_session/', InitiateSession.as_view(), name='initiate_session'),
    path('chat/', Chat.as_view(), name='chat'),
]
