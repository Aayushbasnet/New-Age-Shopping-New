# Generated by Django 3.1.3 on 2021-09-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]