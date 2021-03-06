# Generated by Django 3.2.6 on 2021-08-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gif', '0004_remove_gif_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='gifs',
            field=models.ManyToManyField(blank=True, related_name='categories', to='gif.Gif'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
