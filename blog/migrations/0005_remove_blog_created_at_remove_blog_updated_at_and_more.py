# Generated by Django 4.1.2 on 2022-10-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_created_at_blog_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(verbose_name='Ngày đăng'),
        ),
    ]
