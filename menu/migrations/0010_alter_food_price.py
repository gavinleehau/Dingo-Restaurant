# Generated by Django 4.1.2 on 2022-12-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_food_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20, verbose_name='Giá'),
        ),
    ]