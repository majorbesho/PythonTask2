from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(
        User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)
    who_i = models.TextField(_("about me "), max_length=250)
    price = models.IntegerField(_("price"))
    image = models.ImageField(_("profile"), upload_to='profile')

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name


# Create your models here.
