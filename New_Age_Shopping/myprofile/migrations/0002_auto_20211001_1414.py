# Generated by Django 3.1.3 on 2021-10-01 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myprofile',
            options={'verbose_name_plural': 'Customer Profile'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': 'Shipping Addresses'},
        ),
    ]
