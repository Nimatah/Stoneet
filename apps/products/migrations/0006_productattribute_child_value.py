# Generated by Django 3.1.4 on 2021-03-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210314_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='child_value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
