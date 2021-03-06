from django.db import models
from django.utils import timezone

# python manage.py makemigrations giftcard
# python manage.py migrate giftcard

class Giftcard(models.Model):
    date = models.CharField(max_length=8)
    item_no = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_send = models.BooleanField()
    keyword = models.TextField()
    site = models.TextField()
    title = models.TextField()
    price = models.IntegerField()
    url = models.URLField()

class CrawlerProcess(models.Model):
    server_pid = models.IntegerField()
    crawler_pid = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_run = models.BooleanField()
    args = models.TextField()

class SearchFilter(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_run = models.BooleanField()
    keyword = models.TextField()
    min_price = models.IntegerField()
    max_price = models.IntegerField()