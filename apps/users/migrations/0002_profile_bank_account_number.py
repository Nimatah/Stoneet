# Generated by Django 3.1.4 on 2021-03-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bank_account_number',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
