# Generated by Django 3.2.18 on 2023-04-25 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_booking_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-created_on', 'day', 'time']},
        ),
    ]
