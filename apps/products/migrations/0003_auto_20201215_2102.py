from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201209_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attribute',
            name='view_in_product_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attributes', to='products.attribute'),
        ),
    ]
