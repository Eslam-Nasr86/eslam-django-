from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.


class Post(models.Model):

    title = models.CharField(_(""), max_length=50) 
    content = models.TextField(_(""),max_length=1000)
    create_at =models.DateTimeField(_(""), default=timezone.now)
    image = models.ImageField(_(""), upload_to='post-img/', height_field=None, width_field=None)    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

