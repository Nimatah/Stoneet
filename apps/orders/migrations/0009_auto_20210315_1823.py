# Generated by Django 3.1.4 on 2021-03-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_logisticordermedia_ordermedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('submitted', 'ثبت سفارش'), ('pending_admin', 'در انتظار تایید سایت'), ('pending_seller', 'در انتظار تایید فروشنده'), ('pending_logistic', 'در انتظار تایید حمل و نقل'), ('pending_buyer_logistic_price', 'در انتظار تایید قیمت حمل و نقل توسط خریدار'), ('pending_contract', 'در انتظار تایید قرارداد'), ('pending_finance_documents', 'در انتظار تایید مدارک مالی'), ('accepted', 'تایید نهایی'), ('finished', 'انجام شده')], default='submitted', max_length=255),
        ),
    ]