from django.db import models
from datetime import datetime
from django.contrib.auth.models import User  # this is to add user model
from cloudinary.models import CloudinaryField

# Create your models here.
TIME_CHOICES = (
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30")
)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=200, null=True)
    group_size = models.PositiveIntegerField(null=True, default=1)
    day = models.DateField(default=datetime.now)
    time = models.TimeField(choices=TIME_CHOICES,
                            default="17:00")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["day", "time"]

    def __str__(self):
        return f'{self.user.username} | Group: {self.group_size} | day: {self.day} | time: {self.time}'  # noqa
