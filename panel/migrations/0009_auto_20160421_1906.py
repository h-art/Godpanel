# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 17:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0008_auto_20160421_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='allocation_type',
            field=models.CharField(choices=[('allocation', 'Allocation'), ('pre-allocation', 'Pre allocation'), ('guess', 'Guess')], max_length=50, null=True),
        ),
    ]
