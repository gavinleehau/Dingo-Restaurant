# Generated by Django 4.1.2 on 2022-12-15 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_category_update_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InstagramFeeds',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Danh mục bài viết', 'verbose_name_plural': 'Danh mục bài viết'},
        ),
    ]
