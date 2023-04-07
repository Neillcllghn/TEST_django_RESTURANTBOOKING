from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from datetime import datetime, timedelta
from .models import Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import BookingForm


def index(request):
    return render(request, "index.html")


class BookingList(generic.ListView):
    model = Booking
    template_name = 'bookings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = self.request.user.booking_set.all()
        return context


class BookingCreate(FormView):
    model = Booking
    template_name = 'create_bookings.html'
    form_class = BookingForm
    success_url = 'booking/'

# work in progress
    def register(request):
        form = form_class(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return render(request, 'bookings.html', {'form': form})
