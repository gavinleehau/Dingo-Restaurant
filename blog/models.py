from email.policy import default
from django.urls import reverse
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
import datetime
from datetime import datetime
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from user.models import UserProfile


# Create your models here.

class Category(MPTTModel):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status=models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(default=datetime.now,)
    update_at=models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _("Danh mục bài viết")
        verbose_name_plural = _("Danh mục bài viết")

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.title]  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class author(models.Model):
    author_name = models.CharField('Tên tác giả', default='Dingo Restaurant', max_length=100)
    link = models.CharField('Link nhà hàng', max_length=10000) # This part can be chosen 1 of the two, if you don't need too much detail, just need the restaurant link
    avatar = models.ImageField('Ảnh đại diện', null=True)

    class Meta:
        verbose_name = _("Tác giả")
        verbose_name_plural = _("Tác giả")

    def __str__(self):
        return self.author_name


class blog(models.Model):
    STATUS = (
        (0,"Bản hoàn chỉnh"),
        (1,"Bản thảo")
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,) 
    author     = models.ForeignKey(author, on_delete=models.CASCADE, null=True, verbose_name=_("Tác giả"),)
    title      = models.CharField('Tiêu đề', max_length=1000)
    created_at = models.DateTimeField('Ngày đăng')
    image      = models.ImageField(verbose_name=_("Ảnh đại diện bài viết"))
    content    = RichTextUploadingField('Nội dung')
    status     = models.IntegerField('Trạng thái', choices=STATUS, default=0)

    class Meta:
        ordering = ['-id']
        verbose_name = _("Bài viết")
        verbose_name_plural = _("Bài viết")


    # Custom Admin: Function for show image in Blog
    def image_tag(self):
        return mark_safe('<img src="{}" height="50", width="90px";/>'.format(self.image.url))
    image_tag.short_description='Image'


    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
        return self.created_at

    # class Meta:
    #     verbose_name_plural = _("Tiến Trình Của Người Dùng")

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(blog, on_delete=models.CASCADE, verbose_name=('Bài viết'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=('user'))
    comment = models.TextField(max_length=500, blank=True, verbose_name=('Đánh giá'))
    created_at = models.DateTimeField(default=datetime.now, verbose_name=('Ngày bình luận'))
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=('Ngày cập nhật bình luận'))
    
    class Meta:
        verbose_name = ("Bình luận bài viết")
        verbose_name_plural = ("Bình luận bài viết")
    
    def __str__(self):
        return self.comment


