# Generated by Django 4.1.3 on 2022-12-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakfast',
            name='status',
            field=models.IntegerField(choices=[(0, 'Có'), (1, 'Không có')], default=0, verbose_name='Trạng thái'),
        ),
        migrations.AddField(
            model_name='dinner',
            name='status',
            field=models.IntegerField(choices=[(0, 'Có'), (1, 'Không có')], default=0, verbose_name='Trạng thái'),
        ),
        migrations.AddField(
            model_name='lunch',
            name='status',
            field=models.IntegerField(choices=[(0, 'Có'), (1, 'Không có')], default=0, verbose_name='Trạng thái'),
        ),
        migrations.AddField(
            model_name='special',
            name='status',
            field=models.IntegerField(choices=[(0, 'Có'), (1, 'Không có')], default=0, verbose_name='Trạng thái'),
        ),
        migrations.AlterField(
            model_name='breakfast',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='breakfast',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Ảnh món ăn'),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Ảnh món ăn'),
        ),
        migrations.AlterField(
            model_name='lunch',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lunch',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Ảnh món ăn'),
        ),
        migrations.AlterField(
            model_name='special',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='special',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Ảnh món ăn'),
        ),
    ]
