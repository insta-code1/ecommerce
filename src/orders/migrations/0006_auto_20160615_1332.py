# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_shipping_price',
            new_name='shipping_total_price',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='type',
            field=models.CharField(max_length=120, choices=[(b'billing', b'Billing'), (b'shipping', b'Shipping')]),
        ),
    ]
