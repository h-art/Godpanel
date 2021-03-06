# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('godpanel', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='godpanel.Employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='godpanel.Project')),
            ],
        ),
    ]
