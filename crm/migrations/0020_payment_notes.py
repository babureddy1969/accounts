# Generated by Django 3.0.7 on 2020-12-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_auto_20201202_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='notes',
            field=models.CharField(blank=True, default='Cash', max_length=50, null=True),
        ),
    ]
