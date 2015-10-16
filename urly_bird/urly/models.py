from django.db import models

from django.contrib.auth.models import User
# Create your models here.

# class User(models.Model):
#     user = models.OneToOneField(User)
#     fav_color = models.CharField(max_length=10)



class Click(models.Model):
    author = models.ForeignKey(User, related_name="clicks")
    title = models.CharField(max_length=15)
    timestamp = models.DateTimeField()
    orig = models.CharField(max_length=20)
    short = models.CharField(max_length=20)

    def __str__(self):
         return '{}'.format(self.short)


class Accessed(Click):
    click = models.OneToOneField(Click)
    reader = models.ForeignKey(User)
    accessed_timestamp = models.DateTimeField()
