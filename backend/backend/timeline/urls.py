from django.urls import path, include

from .views import TimelineView

urlpatterns = [
    path('', TimelineView.as_view(), name='timeline')
]