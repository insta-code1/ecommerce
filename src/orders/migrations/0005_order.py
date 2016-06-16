# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_auto_20160613_1003'),
        ('orders', '0004_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_shipping_price', models.DecimalField(default=5.99, max_digits=50, decimal_places=2)),
                ('order_total', models.DecimalField(default=5.99, max_digits=50, decimal_places=2)),
                ('billing_address', models.ForeignKey(related_name='billing_address', to='orders.UserAddress')),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('shipping_address', models.ForeignKey(related_name='shipping_address', to='orders.UserAddress')),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
