from .models import Booking, TIME_CHOICES
from django import forms
from datetime import date, time, datetime
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

# Work in progress

    def clean_future_time_day(self):
        cleaned_data = super(BookingForm, self).clean()
        time = cleaned_data.get('time')
        day = cleaned_data.get('day')
        if time > str(timezone.now()) and day <= date.today():
            return cleaned_data
        else:
            raise ValidationError("You must select a time in the future")

    def clean(self):
        cleaned_data = super(BookingForm, self).clean()
        email = cleaned_data.get('email')
        day = cleaned_data.get('day')
        try:
            Booking.objects.get(email=email, day=day)
        except Booking.DoesNotExist:
            return cleaned_data
        else:
            raise ValidationError(('A booking already exists on that day for '
                                   'the email used'),
                                  code='booking_already_exist')
