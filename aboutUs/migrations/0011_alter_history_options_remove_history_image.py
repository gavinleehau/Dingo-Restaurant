# Generated by Django 4.1.2 on 2022-12-15 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs', '0010_alter_feedback_options_alter_history_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'Giới thiệu nhà hàng', 'verbose_name_plural': 'Giới thiệu nhà hàng'},
        ),
        migrations.RemoveField(
            model_name='history',
            name='image',
        ),
    ]
