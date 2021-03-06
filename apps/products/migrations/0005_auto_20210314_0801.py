# Generated by Django 3.1.4 on 2021-03-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210309_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='has_weight',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='weight_unit',
            field=models.CharField(blank=True, choices=[('کیلوگرم', 'kg'), ('تن', 'ton')], max_length=255),
        ),
    ]
