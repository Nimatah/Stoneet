# Generated by Django 3.1.4 on 2021-06-19 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210316_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticcontent',
            name='about_us',
            field=models.TextField(blank=True),
        ),
    ]
