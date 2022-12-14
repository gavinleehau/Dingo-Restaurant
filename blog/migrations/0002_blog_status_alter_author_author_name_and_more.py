# Generated by Django 4.1.2 on 2022-10-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, verbose_name='Trạng thái'),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(default='Artica Restaurant', max_length=100, verbose_name='Tên tác giả'),
        ),
        migrations.AlterField(
            model_name='author',
            name='link',
            field=models.CharField(max_length=10000, verbose_name='Link nhà hàng'),
        ),
    ]
