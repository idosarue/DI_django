# Generated by Django 3.2.6 on 2021-09-01 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0023_alter_transactionresponse_original_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionresponse',
            name='trade_reciever',
        ),
        migrations.RemoveField(
            model_name='transactionresponse',
            name='trade_sender',
        ),
    ]
