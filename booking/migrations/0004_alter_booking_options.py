# Generated by Django 3.2.18 on 2023-04-02 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['day', 'time']},
        ),
    ]
