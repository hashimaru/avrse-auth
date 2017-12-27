# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-27 01:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_django', '0006_partial'),
        ('eveauth', '0025_auto_20171015_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='character',
            name='token',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_django.UserSocialAuth'),
        ),
    ]
