# Generated by Django 3.2.6 on 2021-08-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gif', '0002_auto_20210817_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='gifs',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
