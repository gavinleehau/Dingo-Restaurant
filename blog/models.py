from email.policy import default
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import datetime

# Create your models here.

class author(models.Model):
    author_name = models.CharField('Tên tác giả', default='Artica Restaurant', max_length=100)
    link        = models.CharField('Link nhà hàng', max_length=10000) # This part can be chosen 1 of the two, if you don't need too much detail, just need the restaurant link
    avatar      = models.ImageField('Ảnh đại diện', null=True)
    # description = RichTextUploadingField('Nội dung')

    def __str__(self):
        return self.author_name

class blog(models.Model):
    STATUS = (
        (0,"Bản thảo"),
        (1,"Bản hoàn chỉnh")
    )
    
    author     = models.ForeignKey(author, on_delete=models.CASCADE, null=True)
    title      = models.CharField('Tiêu đề', max_length=1000)
    created_at = models.DateTimeField('Ngày đăng')
    image      = models.ImageField('Ảnh đại diện bài viết')
    content    = RichTextUploadingField('Nội dung')
    status     = models.IntegerField('Trạng thái', choices=STATUS, default=0)
    note       = models.TextField('Ghi chú', null=True)


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
