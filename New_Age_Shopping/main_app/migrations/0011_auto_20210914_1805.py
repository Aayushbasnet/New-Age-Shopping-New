# Generated by Django 3.1.3 on 2021-09-14 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20210914_1804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['added_date']},
        ),
    ]