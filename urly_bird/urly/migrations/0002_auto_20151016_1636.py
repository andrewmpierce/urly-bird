# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urly', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessed',
            name='accessed_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
