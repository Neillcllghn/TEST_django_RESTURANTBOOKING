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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['bookings'] = self.request.user.booking_set.all()
    #     return context

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingCreate(CreateView):
    model = Booking
    template_name = 'create_bookings.html'
    form_class = BookingForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# work in progress
    # def register(request):
    #     form_class = BookingForm(data=request.POST)
    #     if request.method == 'POST':
    #         if form_class.is_valid():
    #             form_class.save()
    #             return render(request, 'bookings.html', {'form': form})
    #         else:
    #             form_class = BookingForm()
