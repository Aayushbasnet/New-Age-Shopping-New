# Generated by Django 3.1.3 on 2021-09-15 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_shippingaddress_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='order',
        ),
    ]
