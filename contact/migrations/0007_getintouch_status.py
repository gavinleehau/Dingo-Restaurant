# Generated by Django 4.1.3 on 2022-12-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_getintouch'),
    ]

    operations = [
        migrations.AddField(
            model_name='getintouch',
            name='status',
            field=models.IntegerField(choices=[(0, 'Mới'), (1, 'Đã thanh toán')], default=0, verbose_name='Trạng thái'),
        ),
    ]