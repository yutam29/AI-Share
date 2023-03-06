from django.db import models
from accounts.models import Profile
from django.utils import timezone


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    category = models.IntegerField(default=0) # 0:貸出, 1:譲渡, 2:リクエスト
    description = models.TextField(max_length=200, null=True)
    image = models.ImageField(null = True)
    posted_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )


class Comment(models.Model):
    detail = models.TextField(max_length=200)
    cmt_posted_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )

class Lending(models.Model):
    lender = models.ForeignKey(
        Profile,
        on_delete= models.CASCADE,
        related_name='lender',
    )
    item = models.ForeignKey(
        Item,
        on_delete= models.CASCADE,
        related_name='item',
    )
    state = models.IntegerField(default = 0) # 0 : 渡していない状態, 1 : 渡すと決めた状態, 2 : 渡した状態
    posted_at = models.DateTimeField(default=timezone.now)