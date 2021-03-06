# Generated by Django 3.1.4 on 2021-03-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210315_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('submitted', 'ثبت سفارش'), ('pending_admin', 'تایید سایت'), ('pending_seller', 'تایید فروشنده'), ('pending_logistic', 'رد شده'), ('pending_buyer_logistic_price', 'رد شده'), ('pending_contract', 'رد شده'), ('pending_finance_documents', 'رد شده'), ('STATE_ACCEPTED', 'رد شده')], default='submitted', max_length=255),
        ),
    ]
