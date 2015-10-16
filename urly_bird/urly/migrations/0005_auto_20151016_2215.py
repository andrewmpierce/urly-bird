# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('urly', '0004_click_stats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField()),
                ('click', models.ForeignKey(to='urly.Click')),
                ('reader', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='click_stats',
            name='click',
        ),
        migrations.RemoveField(
            model_name='click_stats',
            name='reader',
        ),
        migrations.DeleteModel(
            name='Click_Stats',
        ),
    ]
