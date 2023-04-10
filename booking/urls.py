from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('create/', views.BookingCreate.as_view(), name='create_bookings'),
    path('update/<booking_id>', views.update_booking, name='update_bookings'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
]

urlpatterns += staticfiles_urlpatterns()
