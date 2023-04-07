from .models import Booking, TIME_CHOICES
from django import forms


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
