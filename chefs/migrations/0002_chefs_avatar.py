# Generated by Django 4.1.2 on 2022-10-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefs',
            name='avatar',
            field=models.ImageField(null=True, upload_to='', verbose_name='ảnh đãi diện'),
        ),
    ]
