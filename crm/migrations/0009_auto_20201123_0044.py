# Generated by Django 2.2.10 on 2020-11-22 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20201123_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='date_created',
            new_name='create_date',
        ),
    ]