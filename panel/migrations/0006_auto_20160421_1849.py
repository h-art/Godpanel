# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 16:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_auto_20160421_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='saturation',
            field=models.IntegerField(default=50),
        ),
    ]
