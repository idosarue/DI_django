# Generated by Django 3.2.6 on 2021-08-30 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_topic_topic'),
        ('trading', '0005_auto_20210830_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trading.card')),
                ('trade_reciever', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trade_reciever', to='accounts.profile')),
                ('trade_sender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trade_sender', to='accounts.profile')),
            ],
        ),
    ]
