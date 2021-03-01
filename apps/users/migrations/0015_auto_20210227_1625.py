# Generated by Django 3.1.4 on 2021-02-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210227_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'مرد'), ('female', 'زن')], max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='legal_type',
            field=models.CharField(choices=[('individual', 'حقیقی'), ('legal', 'حقوقی')], default='individual', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(choices=[('pending', 'در حال بررسی'), ('accepted', 'تایید شده'), ('rejected', 'رد شده'), ('banned', 'مسدود شده')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='usermedia',
            name='state',
            field=models.CharField(choices=[('pending', 'در حال بررسی'), ('accepted', 'تایید شده'), ('rejected', 'رد شده')], max_length=255),
        ),
    ]