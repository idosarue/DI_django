# Generated by Django 3.2.6 on 2021-09-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0019_rename_buycardtransaction_sellcardtransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buycardresponse',
            name='coins',
            field=models.IntegerField(default=50),
        ),
    ]
