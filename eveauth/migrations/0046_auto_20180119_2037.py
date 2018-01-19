# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-19 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0045_character_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='alliance',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='eveauth.Alliance'),
        ),
        migrations.AlterField(
            model_name='character',
            name='corp',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='eveauth.Corporation'),
        ),
    ]
