from .models import Booking, TIME_CHOICES
from django import forms
from datetime import date
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

    # def clean_time(self):
    #     time = self.cleaned_data.get('time')
    #     if time < time.now():
    #         raise ValidationError("You must select a time in the future")
    #     return day
