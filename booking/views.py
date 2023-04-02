from django.shortcuts import render, redirect
from django.views import generic, View
from datetime import datetime, timedelta
from .models import Booking
from django.contrib import messages


class BookingList(generic.ListView):
    model = Booking
    template_name = 'bookings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = self.request.user.booking_set.all()
        return context
