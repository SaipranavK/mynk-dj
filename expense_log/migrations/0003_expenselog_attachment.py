# Generated by Django 3.1.1 on 2020-10-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_log', '0002_auto_20201005_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenselog',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
    ]
