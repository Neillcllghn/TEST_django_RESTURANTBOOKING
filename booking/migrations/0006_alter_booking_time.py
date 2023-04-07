# Generated by Django 3.2.18 on 2023-04-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_booking_group_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[('5:00PM', '5:00PM'), ('5:30PM', '5:30PM'), ('6:00PM', '6:00PM'), ('6:30PM', '6:30PM'), ('7:00PM', '7:00PM'), ('7:30PM', '7:30PM'), ('8:00PM', '8:00PM'), ('8:30PM', '8:30PM')], default='5:00 PM', max_length=10),
        ),
    ]