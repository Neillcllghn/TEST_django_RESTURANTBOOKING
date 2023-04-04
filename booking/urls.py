from . import views
from django.urls import path

urlpatterns = [
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('create/', views.BookingCreate.as_view(), name='create_bookings'),
    path('', views.index, name='home'),
]
