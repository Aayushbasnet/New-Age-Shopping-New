# Generated by Django 3.1.3 on 2021-09-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210928_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(blank=True, choices=[('Best', 'Best'), ('Average', 'Average'), ('Poor', 'Poor')], default='Best', max_length=25),
        ),
    ]