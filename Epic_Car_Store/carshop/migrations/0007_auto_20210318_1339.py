# Generated by Django 3.1.7 on 2021-03-18 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0006_product_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
