# Generated by Django 3.1.3 on 2021-09-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210927_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=25),
        ),
    ]