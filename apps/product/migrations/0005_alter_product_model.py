# Generated by Django 4.2.2 on 2023-07-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]