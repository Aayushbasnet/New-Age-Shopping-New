# Generated by Django 3.1.3 on 2021-10-01 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20211001_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level1productcategory',
            options={'verbose_name_plural': 'Level 2 Categories'},
        ),
        migrations.AlterModelOptions(
            name='level2productcategory',
            options={'verbose_name_plural': 'Level 2 Categories'},
        ),
    ]