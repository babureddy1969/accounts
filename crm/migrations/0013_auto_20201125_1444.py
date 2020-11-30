# Generated by Django 2.2.10 on 2020-11-25 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_auto_20201124_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='discount',
            new_name='balance',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='final_cost',
            new_name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_place',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='qty',
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1, null=True)),
                ('cost', models.IntegerField(default=0, null=True)),
                ('final_cost', models.IntegerField(blank=True, default=0, null=True)),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Product')),
            ],
        ),
    ]
