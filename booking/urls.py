from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('create/', views.BookingCreate.as_view(), name='create_bookings'),
]

urlpatterns += staticfiles_urlpatterns()
