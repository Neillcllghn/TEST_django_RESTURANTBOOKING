from django.db import models
from datetime import datetime
from django.contrib.auth.models import User  # this is to add user model
from cloudinary.models import CloudinaryField

# Create your models here.
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


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=200, null=True)
    group_size = models.PositiveIntegerField(null=True, default=1)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES,
                            default="5:00 PM")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["day", "time"]

    def __str__(self):
        return f'{self.user.username} | Group: {self.group_size} | day: {self.day} | time: {self.time}'  # noqa
