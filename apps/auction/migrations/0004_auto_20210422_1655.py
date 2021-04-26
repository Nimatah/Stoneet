# Generated by Django 3.1.4 on 2021-04-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20210422_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='state',
            field=models.CharField(choices=[('started', 'شروع شده'), ('finished', 'تمام شده'), ('expired', 'منقضی شده')], default='started', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='winner',
            field=models.BooleanField(default=False),
        ),
    ]