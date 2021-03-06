# Generated by Django 3.2.6 on 2021-09-02 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210901_1549'),
        ('trading', '0017_card_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyCardTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('A', 'ACCEPT'), ('R', 'REJECT'), ('P', 'PENDING')], default='P', max_length=10)),
                ('trade_choice', models.BooleanField(null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='accounts.profile')),
                ('card', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='card_sell', to='trading.card')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='BuyCardResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_choice', models.BooleanField(null=True)),
                ('coins', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='buy_response', to='accounts.profile')),
                ('original_transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trading.buycardtransaction')),
            ],
        ),
    ]
