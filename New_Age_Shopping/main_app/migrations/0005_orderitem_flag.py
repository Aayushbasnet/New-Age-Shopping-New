# Generated by Django 3.1.3 on 2021-09-14 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210914_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='flag',
            field=models.IntegerField(default=0),
        ),
    ]
