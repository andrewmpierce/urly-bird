# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urly', '0002_auto_20151016_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessed',
            name='click',
        ),
        migrations.RemoveField(
            model_name='accessed',
            name='reader',
        ),
        migrations.AddField(
            model_name='click',
            name='accessed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='click',
            name='orig',
            field=models.URLField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Accessed',
        ),
    ]
