# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from . import views


urlpatterns = [
    path('chat', views.chat, name='chat'),
    path('chat/<int:room_id>/', views.room, name='room'),
    path('make_room/<int:item_id>/', views.making_room, name='making_room'),
]