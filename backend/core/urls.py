"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import PointersView, AudioURLView, ImageURlView, GetAvatarURLView, CreateVideoView, TimelineView, FlashCardView, GetLearningModuleView, SaveAvatarURLView,SaveVideoView

urlpatterns = [
    path('send-pointer', PointersView.as_view(), name='send-pointer'),
    path('save-video',SaveVideoView.as_view(), name='save-video'),
    path('create-avatar', ImageURlView.as_view(), name='create-avatar'),
    path('save-avatar', SaveAvatarURLView.as_view(), name='save-avatar'),
    path('get-avatar', GetAvatarURLView.as_view(), name='get-avatar'),
    path('create-video', CreateVideoView.as_view(), name='create-video'),
    path('timeline', TimelineView.as_view(), name='timeline'),
    path('flashcard', FlashCardView.as_view(), name='flashcard'),
    path('get-learning-module', GetLearningModuleView.as_view(), name='get-learning-module')
]
