# Generated by Django 4.1.2 on 2022-10-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs', '0006_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='customer_avatar',
            field=models.ImageField(null=True, upload_to='', verbose_name='Ảnh đại diện khách hàng'),
        ),
    ]