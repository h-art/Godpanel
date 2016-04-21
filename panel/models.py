from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.utils import timezone

from django.db import models
from datetime import datetime


class Area(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    full_name = models.CharField(max_length=80)
    email = models.EmailField()
    area = models.ForeignKey('Area', null=True)
    role = models.ForeignKey('Role', null=True)

    def __unicode__(self):
        return self.email

class Project(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey('Client', null=True)

    def __unicode__(self):
        return self.name

class Allocation(models.Model):
    ALLOCATION = 'allocation'
    PRE_ALLOCATION = 'pre-allocation'
    GUESS = 'guess'

    ALLOCATION_TYPES = (
        (ALLOCATION, 'Allocation'),
        (PRE_ALLOCATION, 'Pre allocation'),
        (GUESS, 'Guess'),
    )

    start = models.DateField()
    end = models.DateField()
    employee = models.ForeignKey('Employee')
    project = models.ForeignKey('Project')
    saturation = models.IntegerField(default=100)
    note = models.TextField(null=True, blank=True)
    allocation_type = models.CharField(max_length=50,
        choices=ALLOCATION_TYPES, null=True, default=ALLOCATION)
