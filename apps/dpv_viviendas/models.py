from django.db import models
from apps.dpv_nomencladores.models import Destino
from apps.dpv_persona.models import PersonaNatural


# Create your models here.
class Concepto(models.Model):
    nombre = models.CharField(max_length=25, verbose_name="Concepto")

    class Meta:
        verbose_name = "Concepto"
        verbose_name_plural = "Conceptos"
        ordering = ["nombre", ]

    def __str__(self):
        return self.nombre


class Vivienda(models.Model):
    numero = models.PositiveSmallIntegerField()
    destino = models.ForeignKey(Destino, help_text="Destino para la vivienda", related_name="locales_dest", on_delete=models.CASCADE)
    cantidad_persona = models.PositiveSmallIntegerField(help_text="Cantidad de personas que viven en la vivienda")
    propietario = models.ForeignKey(PersonaNatural, related_name="vivienada_prop", on_delete=models.CASCADE)
    fecha_propietario = models.DateField(verbose_name="Fecha de habitado", auto_now=False, auto_now_add=False)
    concepto = models.ForeignKey(Concepto, verbose_name="Concepto", help_text="Concepto de uso de la vivienda", on_delete=models.CASCADE)
    aprobada = models.BooleanField(default=False, verbose_name="Aprobación dada", help_text="Marcar si la vivienda esta aprobada")
    add_concepto = models.CharField(max_length=20, verbose_name="Datos Concepto", blank=True)

    class Meta:
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"
        ordering = ['numero']

    def __str__(self):
        return str(self.numero)
