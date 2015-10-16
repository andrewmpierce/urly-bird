from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Click(models.Model):
    author = models.ForeignKey(User, related_name="clicks")
    title = models.CharField(max_length=15)
    timestamp = models.DateTimeField(null=True)
    accessed = models.IntegerField(default=0)
    orig = models.URLField(max_length=50)
    short = models.CharField(max_length=20)
    data = {}


    def __str__(self):
         return '{}'.format(self.short)

    def record(time, user, request):
        Click.data[user] = time


class Stats(models.Model):
    reader = models.ForeignKey(User)
    click = models.ForeignKey(Click)
    timestamp = models.DateTimeField()

    def __str__(self):
        return '{} @ {}'.format(self.reader, self.timestamp)
