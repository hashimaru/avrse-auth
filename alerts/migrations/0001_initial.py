# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-13 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('structure_reinforce', 'Structure Reinforce')], db_index=True, max_length=64)),
                ('url', models.CharField(max_length=512)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
