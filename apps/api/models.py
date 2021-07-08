from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings

import uuid

class Profile(models.Model):
    """
    Profile for Django User class
    """
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                verbose_name='Usuário', 
                                on_delete=models.CASCADE)
    extrainfo = models.UUIDField(default=uuid.uuid4, auto_created=True)

    objects = models.manager.Manager()

    def __str__(self):
        # pylint: disable=E1101
        return "Profile: " + self.usuario.username
    

class Registro(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                verbose_name='Usuário', 
                                on_delete=models.CASCADE)
    descricao = models.CharField(_("Descrição"), max_length=200)
    timestamp = models.DateTimeField(_("Data de criação"), auto_now_add=True)

    objects = models.manager.Manager()

    class Meta:
        verbose_name = _("registro")
        verbose_name_plural = _("registros")
    
    def __str__(self):
        return self.timestamp


