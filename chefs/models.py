from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Chefs(models.Model):
    POSITION = (
        ("Bếp trưởng", "Bếp trưởng"),
        ("Bếp phó", "Bếp phó")
    )

    fullName     = models.CharField(verbose_name  = _("Tên đầu bếp"), max_length=50)
    avatar       = models.ImageField(verbose_name = _("ảnh đãi diện"), null=True)
    position     = models.CharField(verbose_name = _('Vị trí'), choices=POSITION, max_length=50)
    yearOfBirth  = models.DateField(verbose_name = _("Năm sinh"), null=True)
    homeTown     = models.CharField(verbose_name = _("Quê quán"), max_length=1000)
    joiningDate  = models.DateField(verbose_name = _("Ngày tham gia"), null=True)
    # social
    faceBook  = models.CharField("Facebook", default="#", max_length=1000, blank=True)
    twitter   = models.CharField("Twiiter", default="#", max_length=1000, blank=True)
    instagram = models.CharField("Instagram", default="#", max_length=1000, blank=True)
    skype     = models.CharField("Skype", default="#", max_length=1000, blank=True)

    class Meta:
        verbose_name = _("Đầu bếp")
        verbose_name_plural = _("Đầu bếp")

    def __str__(self):
        return self.fullName