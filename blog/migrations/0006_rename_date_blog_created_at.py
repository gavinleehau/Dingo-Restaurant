# Generated by Django 4.1.2 on 2022-10-07 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blog_created_at_remove_blog_updated_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date',
            new_name='created_at',
        ),
    ]
