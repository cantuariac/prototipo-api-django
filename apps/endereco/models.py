from django.db import models
from django.utils.translation import gettext as _


# class Localidade(models.Model):

#     cidade = models.TextField(_("Cidade"))
#     bairro = models.TextField(_("Bairro"))
#     logradouro = models.TextField(_("Logradouro"))
#     numero = models.PositiveSmallIntegerField(_("Número"))

#     latitude = models.FloatField(_("Latitude"))
#     longitude = models.FloatField(_("Longitude"))

#     class Meta:
#         verbose_name = _("Localidade")
#         verbose_name_plural = _("Localidades")

#     def __str__(self):
#        return f"{self.logradouro}, {self.numero}, {self.bairro}"

class Estado(models.Model):
    codigo = models.CharField(_("Código"), max_length=2)
    nome = models.CharField(_("Nome"), max_length=50)

class Cidade(models.Model):
    nome = models.CharField(_("Nome"), max_length=50)
    estado = models.ForeignKey("endereco.Estado", verbose_name=_("Estado"), on_delete=models.CASCADE)

class Bairro(models.Model):
    nome = models.CharField(_("Nome"), max_length=50)
    Cidade = models.ForeignKey("endereco.Cidade", verbose_name=_("Cidade"), on_delete=models.CASCADE)

class Logradouro(models.Model):
    nome = models.CharField(_("Nome"), max_length=50)
    cep = models.CharField(_("CEP"), max_length=10)
    bairro = models.ForeignKey("endereco.Bairro", verbose_name=_("Bairro"), on_delete=models.CASCADE)

class Endereco(models.Model):
    numero = models.CharField(_("Número"), max_length=10)
    logradouro = models.ForeignKey("endereco.Logradouro", verbose_name=_("Logradouro"), on_delete=models.CASCADE)
    latitude = models.FloatField(_("Latitude"), null=True, default=None)
    longitude = models.FloatField(_("Longitude"), null=True, default=None)

