from __future__ import unicode_literals
from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=80, default='')
    last_name = models.CharField(max_length=80, default='')
    email = models.EmailField()
    area = models.ForeignKey('Area', null=True)
    role = models.ForeignKey('Role', null=True)

    def __str__(self):
        return ' - '.join([self.email,
                           ' '.join((self.first_name, self.last_name))])

    class Meta:
        # this will make ordering by last name default *always*
        ordering = ['last_name']


class Project(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey('Client', null=True)

    def __str__(self):
        return ' - '.join([self.client.name, self.name])


class ClosingDay(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')


class Allocation(models.Model):
    ALLOCATION = 'allocation'
    PRE_ALLOCATION = 'pre-allocation'
    GUESS = 'guess'
    OFF_REQUEST = 'off_request'
    OFF = 'off'

    ALLOCATION_TYPES = (
        (ALLOCATION, 'Allocazione'),
        (PRE_ALLOCATION, 'Pre allocazione'),
        (GUESS, 'Guess'),
        (OFF_REQUEST, 'Richiesta time-off'),
        (OFF, 'Time-off'),
    )

    start = models.DateField()
    end = models.DateField()
    employee = models.ForeignKey('Employee')
    project = models.ForeignKey('Project')
    saturation = models.IntegerField(default=100)
    note = models.TextField(null=True, blank=True)
    allocation_type = models.CharField(max_length=50,
                                       choices=ALLOCATION_TYPES,
                                       null=True,
                                       default=ALLOCATION)
