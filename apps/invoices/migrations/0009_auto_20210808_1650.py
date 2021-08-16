# Generated by Django 3.1.4 on 2021-08-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_invoice_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='guaranty',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]