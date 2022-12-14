# Generated by Django 4.1.3 on 2022-12-11 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_alter_blog_options_alter_blog_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=500, verbose_name='Đánh giá')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày bình luận')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày cập nhật bình luận')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='Bài viết')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Đánh giá bài viết',
                'verbose_name_plural': 'Đánh giả bài viết',
            },
        ),
    ]
