# Generated by Django 2.2.10 on 2020-11-25 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20201125_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Customer'),
        ),
    ]