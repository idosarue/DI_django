# Generated by Django 3.2.6 on 2021-09-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0012_transaction_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='price',
            field=models.IntegerField(default=50),
        ),
    ]
