# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('urly', '0003_auto_20151016_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click_Stats',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('click', models.ForeignKey(to='urly.Click')),
                ('reader', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
