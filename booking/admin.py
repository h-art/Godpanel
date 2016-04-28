from django.contrib import admin
from .models import Room, Applicant, Booking


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'office', 'seats')
    list_filter = ('office',)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_description', 'start_date')
    list_filter = ('room',)


admin.site.register(Room, RoomAdmin)
admin.site.register(Applicant)
admin.site.register(Booking, BookingAdmin)