# Generated by Django 2.2.10 on 2020-11-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20201026_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='gms',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='size',
            new_name='details',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18, null=True),
        ),
    ]
