# Generated by Django 3.2.18 on 2023-04-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30')], default='17:00', max_length=10),
        ),
    ]