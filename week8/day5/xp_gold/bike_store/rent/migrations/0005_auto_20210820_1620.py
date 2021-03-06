# Generated by Django 3.2.6 on 2021-08-20 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_alter_customer_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=80)),
                ('address2', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='real',
            field=models.IntegerField(default=500),
        ),
        migrations.CreateModel(
            name='RentalStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('capacity', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.address')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='city_address', to='rent.address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='country_address', to='rent.address'),
        ),
    ]
