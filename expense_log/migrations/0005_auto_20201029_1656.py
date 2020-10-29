# Generated by Django 3.1.1 on 2020-10-29 16:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_log', '0004_auto_20201029_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenselog',
            name='amount',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
    ]