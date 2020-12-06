# Generated by Django 3.0.7 on 2020-12-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_remove_product_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='making_charges',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=1, null=True),
        ),
    ]