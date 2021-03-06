# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('area', models.CharField(choices=[('DEV', 'Developer'), ('ART', 'Art'), ('UX', 'Interaction design')], max_length=10)),
            ],
        ),
    ]
