from .models import Booking, TIME_CHOICES
from django import forms
from datetime import datetime, date, time
from django.utils import timezone
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('email', 'group_size', 'day', 'time',)
        labels = {
            'day': 'Select reservation date',
            'time': 'Select time of reservation'
        }

        widgets = {
            'day': forms.DateInput(attrs={'class': 'form-control',
                                   'type': 'date'}),
            'time': forms.TimeInput(attrs={'format': '%H',
                                    'class': 'form-control', 'type': 'time'})
        }

    def clean_group_size(self):
        group_size = self.cleaned_data.get('group_size')
        if int(group_size) < 1 or int(group_size) > 6:
            raise ValidationError(f"You selected {group_size}, "
                                  "please select between 1 and 6 guests")
        return group_size

    def clean_day(self):
        day = self.cleaned_data.get('day')
        if day < date.today():
            raise ValidationError("You must select today's date "
                                  "or a future date")
        return day

    def clean_future_time_day(self):
        cleaned_data = super(BookingForm, self).clean()
        time = cleaned_data.get('time')
        day = cleaned_data.get('day')

        if day and time:
            current_date = timezone.localtime(timezone.now()).date()
            current_time = timezone.localtime(timezone.now()).time()

            if day > current_date:
                return cleaned_data
            elif day == current_date and time > str(current_time):
                return cleaned_data
            else:
                raise ValidationError("You must select a time in the future")
        else:
            raise ValidationError("The Time selected is incorrect")

    def clean(self):
        email = self.cleaned_data.get('email')
        day = self.cleaned_data.get('day')

        self.clean_future_time_day()

        if hasattr(self, 'instance'):
            booking_all = Booking.objects.exclude(
                email=self.instance.email).filter(email=email)
        else:
            booking_all = Booking.objects.all().filter(email=email)
        for item in booking_all:
            if day == item.day and email == item.email:
                raise forms.ValidationError("A booking already exists on "
                                            "that day for the email used")
