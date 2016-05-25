# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godpanel', '0012_auto_20160424_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosingDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='allocation',
            name='allocation_type',
            field=models.CharField(choices=[('allocation', 'Allocazione'), ('pre-allocation', 'Pre allocazione'), ('guess', 'Guess'), ('off_request', 'Richiesta time-off'), ('off', 'Time-off')], default='allocation', max_length=50, null=True),
        ),
    ]