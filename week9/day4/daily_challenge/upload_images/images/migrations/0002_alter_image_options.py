# Generated by Django 3.2.6 on 2021-08-25 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-timestamp']},
        ),
    ]
