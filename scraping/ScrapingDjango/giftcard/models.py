from django.db import models
from django.utils import timezone


class Giftcard(models.Model):
    date = models.CharField(max_length=8)
    item_no = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    is_send = models.BooleanField()
    keyword = models.TextField()
    site = models.TextField()
    title = models.TextField()
    price = models.IntegerField()
    link = models.URLField()