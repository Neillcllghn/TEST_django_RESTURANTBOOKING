from . import views
from django.urls import path

urlpatterns = [
    path('', BookingDetails.as_view(), name='home'),
]
