# Generated by Django 4.1.2 on 2022-12-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userprofile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên Nhân viên:')),
                ('email', models.CharField(max_length=200, verbose_name='Email Nhân viên:')),
                ('phone', models.CharField(max_length=20, verbose_name='Số điện thoại')),
                ('BirthDate', models.DateField(verbose_name='Ngày sinh')),
                ('gender', models.IntegerField(choices=[(0, 'Nam'), (1, 'Nữ')], default=0, verbose_name='Giới tính')),
                ('citizenshipCard', models.CharField(max_length=100, verbose_name='Số thẻ CCCD/CMND:')),
                ('homeTown', models.CharField(max_length=100, verbose_name='Quê quán:')),
                ('joinedDate', models.DateField(verbose_name='Ngày vào làm')),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive')], default=0, verbose_name='Trạng thái')),
            ],
            options={
                'verbose_name': 'Nhân viên',
                'verbose_name_plural': 'Nhân viên',
            },
        ),
    ]
