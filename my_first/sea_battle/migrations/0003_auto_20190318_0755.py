# Generated by Django 2.1.7 on 2019-03-18 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sea_battle', '0002_auto_20190318_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_connect_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 7, 55, 23, 400413)),
        ),
        migrations.AlterField(
            model_name='player',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 7, 55, 23, 400321)),
        ),
    ]