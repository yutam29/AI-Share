from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user_name = models.CharField(max_length=50)
    room_number = models.CharField(max_length = 4)
    profile_image = models.ImageField(null = True, default='icons/neko.jpg')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )