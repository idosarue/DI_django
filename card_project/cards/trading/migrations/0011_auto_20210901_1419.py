# Generated by Django 3.2.6 on 2021-09-01 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_topic_topic'),
        ('trading', '0010_remove_transaction_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='card1', to='trading.card'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='choice',
            field=models.CharField(choices=[('A', 'ACCEPT'), ('R', 'REJECT'), ('P', 'PENDING')], default='P', max_length=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='trade_choice',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='trade_reciever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_target', to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='trade_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_offer', to='accounts.profile'),
        ),
        migrations.CreateModel(
            name='TransactionResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_choice', models.BooleanField(null=True)),
                ('card', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trades_respone', to='trading.card')),
                ('original_transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trading.transaction')),
            ],
        ),
    ]