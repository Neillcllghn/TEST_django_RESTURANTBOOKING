from django.contrib import admin
from .models import Booking

# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('user', 'email', 'day', 'time', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['user', 'email']
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
