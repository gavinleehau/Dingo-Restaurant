# Generated by Django 4.1.2 on 2022-12-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_food_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': 'Thực đơn món', 'verbose_name_plural': 'Thực đơn món'},
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(verbose_name='Mô tả món ăn'),
        ),
    ]