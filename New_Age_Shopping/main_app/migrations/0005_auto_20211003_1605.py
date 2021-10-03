# Generated by Django 3.1.3 on 2021-10-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20211001_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'ordering': ('-payment_update',), 'verbose_name_plural': 'Shipping Addresses'},
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='payment_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
