# Generated by Django 4.1.1 on 2022-10-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='dni',
        ),
        migrations.AddField(
            model_name='client',
            name='dpi',
            field=models.CharField(default=2, max_length=10, unique=True, verbose_name='Dpi'),
            preserve_default=False,
        ),
    ]
