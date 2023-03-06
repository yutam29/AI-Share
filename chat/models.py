from django.db import models
from accounts.models import Profile
from django.utils import timezone

# Create your models here.

class ChatRoom(models.Model):
    user1 = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='user1',
    )
    user2 = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='user2',
    )
    latest_date = models.DateTimeField(default=timezone.now)

class Chat(models.Model):
    sender = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    text = models.TextField(max_length=200)
    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
    )
    