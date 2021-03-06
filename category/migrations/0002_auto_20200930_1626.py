# Generated by Django 3.1.1 on 2020-09-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='value',
            field=models.PositiveIntegerField(default=0, help_text='Maximum spending in this category from total monthly expense', verbose_name='Category Limit'),
        ),
    ]
