# Generated by Django 3.1.4 on 2021-03-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productattribute_child_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='has_child_value',
            field=models.BooleanField(default=False),
        ),
    ]