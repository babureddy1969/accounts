# Generated by Django 3.0.7 on 2020-12-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0027_order_gold_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='gold_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='wt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]