# Generated by Django 3.1.7 on 2021-04-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0013_product_carimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='carimg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
