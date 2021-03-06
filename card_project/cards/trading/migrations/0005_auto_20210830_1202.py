# Generated by Django 3.2.6 on 2021-08-30 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0004_auto_20210830_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peoplecard',
            name='id',
        ),
        migrations.RemoveField(
            model_name='vehiclecard',
            name='id',
        ),
        migrations.AddField(
            model_name='peoplecard',
            name='card_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trading.card'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclecard',
            name='card_ptr',
            field=models.OneToOneField(auto_created=True, default=2, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trading.card'),
            preserve_default=False,
        ),
    ]
