# Generated by Django 3.2.18 on 2023-04-01 11:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, null=True)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('5:00PM', '5:00PM'), ('5:30PM', '5:30PM'), ('6:00PM', '6:00PM'), ('6:30PM', '6:30PM'), ('7:00PM', '7:00PM'), ('7:30PM', '7:30PM'), ('8:00PM', '8:00PM'), ('8:30PM', '8:30PM')], default='5:00 PM', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
