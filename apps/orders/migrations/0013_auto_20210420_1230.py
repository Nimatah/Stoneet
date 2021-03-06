# Generated by Django 3.1.4 on 2021-04-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20210420_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='reject_reason',
            field=models.TextField(blank=True),
        ),
    ]
