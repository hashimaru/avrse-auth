# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-14 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0053_character_clone_jump_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='fuel_notifications',
            field=models.BooleanField(default=False),
        ),
    ]