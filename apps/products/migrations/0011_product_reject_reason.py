# Generated by Django 3.1.4 on 2021-04-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210420_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reject_reason',
            field=models.TextField(blank=True),
        ),
    ]