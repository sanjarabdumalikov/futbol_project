# Generated by Django 4.2.3 on 2023-07-28 05:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futbool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('addres', models.CharField(default='', max_length=50)),
                ('contact', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(upload_to='upolad/Place')),
                ('booking_place_per_hour', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_time', models.TimeField(default=datetime.datetime.now)),
                ('ending_time', models.TimeField(default=datetime.datetime.now)),
                ('start_free_time', models.TimeField(blank=True, null=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='futbool.place')),
            ],
        ),
    ]
