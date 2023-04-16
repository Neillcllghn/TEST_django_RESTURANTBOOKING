from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from datetime import datetime, timedelta
from .models import Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, CreateView
from .forms import BookingForm


def index(request):
    return render(request, "index.html")


class BookingList(generic.ListView):
    model = Booking
    template_name = 'bookings.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingCreate(CreateView):
    model = Booking
    template_name = 'create_bookings.html'
    form_class = BookingForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.INFO,
                             'Booking was made successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'update_bookings.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('bookings')
