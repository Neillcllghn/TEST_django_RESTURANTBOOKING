from django.shortcuts import render, redirect
from django.views import generic, View
from datetime import datetime, timedelta
from .models import Booking
from django.contrib import messages


class BookingDetails(View):
    model = Booking
    context = {
        'day': day,
        'time': time
    }

    def index(request):
        return render(request, "bookings.html", context)
