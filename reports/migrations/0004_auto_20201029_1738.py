# Generated by Django 3.1.1 on 2020-10-29 17:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20201029_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='daily_avg',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='report',
            name='savings',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='categorysnap',
            name='spent',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='report',
            name='total_exp',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
