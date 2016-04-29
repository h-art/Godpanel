from django.db import models
from django.utils import timezone


class Room(models.Model):
    OFFICES = (
        ("Treviso", 'Treviso'),
        ("Milano", 'Milano'),
    )
    name = models.CharField(max_length=200)
    seats = models.IntegerField()
    office = models.CharField(max_length=20,
                              choices=OFFICES,
                              default="Treviso", blank=False)
    note = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Applicant(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Booking(models.Model):
    title = models.CharField(max_length=250, null=False)
    request_by = models.ForeignKey('Applicant')
    room = models.ForeignKey('Room')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    num_partecipants = models.IntegerField()
    note = models.TextField()

    def get_description(self):
        return self.room.name + " (da " + self.request_by.last_name + ")"

    def __str__(self):
        return self.get_description()
