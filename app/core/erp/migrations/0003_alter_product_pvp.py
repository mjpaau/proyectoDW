# Generated by Django 4.1.1 on 2022-10-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_remove_product_cate_product_cat_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de venta'),
        ),
    ]
