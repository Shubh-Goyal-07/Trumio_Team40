from django.urls import path, include
from .views import PointersView, ImageURlView, GetAvatarURLView, CreateVideoView, FlashCardView, GetLearningModuleView, SaveAvatarURLView, SaveVideoView
urlpatterns = [
    path('send-pointer', PointersView.as_view(), name='send-pointer'),
    path('save-video',SaveVideoView.as_view(), name='save-video'),
    path('create-avatar', ImageURlView.as_view(), name='create-avatar'),
    path('save-avatar', SaveAvatarURLView.as_view(), name='save-avatar'),
    path('get-avatar', GetAvatarURLView.as_view(), name='get-avatar'),
    path('create-video', CreateVideoView.as_view(), name='create-video'),
    path('flashcard', FlashCardView.as_view(), name='flashcard'),
    path('get-learning-module', GetLearningModuleView.as_view(), name='get-learning-module')
]