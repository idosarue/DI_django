# Generated by Django 3.2.6 on 2021-08-30 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0010_remove_transaction_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='card',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner_deck', to='trading.card'),
        ),
    ]