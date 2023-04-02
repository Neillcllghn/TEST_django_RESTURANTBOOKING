from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.BookingList.as_view(), name='bookings'),
]
