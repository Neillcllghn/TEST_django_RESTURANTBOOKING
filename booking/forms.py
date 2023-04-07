from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('email', 'group_size', 'day', 'time',)
        TIME_CHOICES = (
                ("5:00PM", "5:00PM"),
                ("5:30PM", "5:30PM"),
                ("6:00PM", "6:00PM"),
                ("6:30PM", "6:30PM"),
                ("7:00PM", "7:00PM"),
                ("7:30PM", "7:30PM"),
                ("8:00PM", "8:00PM"),
                ("8:30PM", "8:30PM")
                )
        labels = {
            'day': 'Select reservation date', 
            'time': 'Select time of reservation'
        }

        widgets = {
            'day': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TextInput(attrs={'format':'%H', 'class': 'form-control', 'type': 'time', 'required step': "0"})
        }
