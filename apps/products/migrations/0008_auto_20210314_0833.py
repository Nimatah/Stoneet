# Generated by Django 3.1.4 on 2021-03-14 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_attribute_has_child_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='weight_unit',
            field=models.CharField(blank=True, choices=[('kg', 'کیلوگرم'), ('ton', 'تن')], max_length=255),
        ),
    ]
