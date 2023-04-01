from django.shortcuts import render, redirect
from django.views import generic, View
from datetime import datetime, timedelta
from .models import Booking
from django.contrib import messages


class BookingDetails(View):
    model = Booking

    def index(request):
        return render(request, "base.html")
