# Generated by Django 3.2.6 on 2021-08-31 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0018_transaction_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='trade_choice',
            field=models.BooleanField(null=True),
        ),
    ]
