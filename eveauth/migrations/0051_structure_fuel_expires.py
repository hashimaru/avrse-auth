# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-11 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0050_auto_20180311_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='fuel_expires',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
