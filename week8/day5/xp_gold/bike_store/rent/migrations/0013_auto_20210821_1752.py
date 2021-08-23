# Generated by Django 3.2.6 on 2021-08-21 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0012_auto_20210821_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(default=1, max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='home_address', to='rent.address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(default=1, max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='city_address', to='rent.address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.ForeignKey(default=1, max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='country_address', to='rent.address'),
        ),
    ]
