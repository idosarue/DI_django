# Generated by Django 3.2.6 on 2021-08-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0009_alter_vehicleatrentalstation_departure_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
    ]
