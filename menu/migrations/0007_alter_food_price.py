# Generated by Django 4.1.2 on 2022-12-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_rename_special_food_delete_breakfast_delete_dinner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
    ]
