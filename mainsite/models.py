from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class AccessInfo(models.Model):
    access_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-access_time',)

    def __str__(self):
        return self.access_time