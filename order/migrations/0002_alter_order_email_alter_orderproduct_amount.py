# Generated by Django 4.1.2 on 2022-12-14 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
