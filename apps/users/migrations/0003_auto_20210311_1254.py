# Generated by Django 3.1.4 on 2021-03-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bank_account_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='distance_to_road',
        ),
        migrations.RemoveField(
            model_name='address',
            name='load_tools',
        ),
        migrations.RemoveField(
            model_name='address',
            name='proper_road',
        ),
        migrations.RemoveField(
            model_name='address',
            name='road_name',
        ),
        migrations.AddField(
            model_name='address',
            name='postal_code',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
