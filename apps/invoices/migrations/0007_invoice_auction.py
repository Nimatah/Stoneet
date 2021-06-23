# Generated by Django 3.1.4 on 2021-06-21 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20210423_1425'),
        ('invoices', '0006_invoice_logistic_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auction.auction'),
        ),
    ]