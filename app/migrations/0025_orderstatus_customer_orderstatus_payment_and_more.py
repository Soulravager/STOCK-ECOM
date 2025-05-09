# Generated by Django 5.1.2 on 2025-04-15 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_orderstatus_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatus',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer'),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.payment'),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='delivery_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='order_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='ordered_date',
            field=models.DateTimeField(),
        ),
    ]
