# Generated by Django 3.2.6 on 2021-08-22 11:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_film_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 22, 11, 10, 59, 108421, tzinfo=utc)),
        ),
    ]
