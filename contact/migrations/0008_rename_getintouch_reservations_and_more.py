# Generated by Django 4.1.3 on 2022-12-06 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_getintouch_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='getInTouch',
            new_name='Reservations',
        ),
        migrations.AlterModelOptions(
            name='reservations',
            options={'verbose_name': 'Đặt bàn', 'verbose_name_plural': 'Đặt bàn'},
        ),
    ]
