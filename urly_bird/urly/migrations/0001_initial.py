# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField()),
                ('orig', models.CharField(max_length=20)),
                ('short', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Accessed',
            fields=[
                ('click', models.OneToOneField(primary_key=True, to='urly.Click', serialize=False)),
                ('accessed_timestamp', models.DateTimeField()),
                ('reader', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('urly.click',),
        ),
        migrations.AddField(
            model_name='click',
            name='author',
            field=models.ForeignKey(related_name='clicks', to=settings.AUTH_USER_MODEL),
        ),
    ]
