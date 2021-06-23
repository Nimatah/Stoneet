# Generated by Django 3.1.4 on 2021-06-21 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0007_invoice_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='type',
            field=models.CharField(blank=True, choices=[('seller', 'فروشنده'), ('buyer', 'خریدار'), ('logistic', 'باربری')], max_length=255, null=True),
        ),
    ]
