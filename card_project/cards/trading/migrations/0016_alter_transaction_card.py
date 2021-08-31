# Generated by Django 3.2.6 on 2021-08-31 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0015_auto_20210830_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='trading.card'),
        ),
    ]