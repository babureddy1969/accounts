# Generated by Django 3.0.7 on 2020-12-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0022_auto_20201206_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]