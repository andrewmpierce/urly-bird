from django.db import models


# Create your models here.


class Url_user(models.Model):
    username = models.CharField(max_length=60)


class Click(models.Model):
    click_id = models.ForeignKey(URl_user)
    title = models.CharField(max_length=40)
    desc = models.CharField(max_length=160)
    orig_timestamp = models.DateTimeField(auto_now_add=True)

class Accessed(models.Model):
    accessed_id = models.ForeignKey(Click)
    new_timestamp = models.DateTimeStamp(auto_now=True)
    click_count = models.SmallIntegerField()
