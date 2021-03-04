# Generated by Django 3.1.4 on 2021-03-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210227_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='mine',
            name='location_in_region',
            field=models.CharField(choices=[('north', 'شمال'), ('south', 'جنوب'), ('east', 'شرق'), ('west', 'غرب')], default='north', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(choices=[('pending', 'در انتظار تایید'), ('accepted', 'تایید شده'), ('rejected', 'رد شده'), ('banned', 'مسدود شده')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='usermedia',
            name='state',
            field=models.CharField(choices=[('pending', 'در انتظار تایید'), ('accepted', 'تایید شده'), ('rejected', 'رد شده')], default='pending', max_length=255),
        ),
    ]
