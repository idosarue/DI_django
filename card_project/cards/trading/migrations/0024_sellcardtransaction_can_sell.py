# Generated by Django 3.2.6 on 2021-09-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0023_alter_sellcardtransaction_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellcardtransaction',
            name='can_sell',
            field=models.BooleanField(default=True),
        ),
    ]
