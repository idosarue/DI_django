# Generated by Django 3.2.6 on 2021-08-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_completion',
            field=models.DateTimeField(null=True),
        ),
    ]
