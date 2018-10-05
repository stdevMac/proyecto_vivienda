from django.db import models
from apps.nomencladores.models import Municipio, Organismo, Calle, Piso
from .validators import validate_acta_acuerdo


# Create your models here.
class Local(models.Model):
    direccion_calle = models.ForeignKey(Calle, related_name="calle_principal", help_text="Calle de la direccion", on_delete=models.CASCADE, verbose_name="Calle")
    direccion_numero = models.CharField(max_length=10, help_text="Numero de la dirección", verbose_name="Número")
    piso = models.ForeignKey(Piso, help_text="Piso de la direccion del local", on_delete=models.CASCADE)
    direccion_entre1 = models.ForeignKey(Calle, related_name="entrecalle1", verbose_name="Primera Entrecalle", max_length=50, help_text="Primera entre calle de la dirección", on_delete=models.CASCADE)
    direccion_entre2 = models.ForeignKey(Calle, related_name="entrecalle2", verbose_name="Segunda Entrecalle", max_length=50, help_text="Segunda entre calle de la dirección", on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, related_name="locales_mun", help_text="Municipio donde se encuentra ubicado el local el local", on_delete="Null")
    no_viviendas = models.PositiveSmallIntegerField(verbose_name="Total de viviendas", help_text="Total de viviendas en el local")
    aprobado = models.BooleanField(default=False, help_text="Marque si está aprobado el local")
    pendiente = models.PositiveSmallIntegerField(verbose_name="Pendientes de aprobación", help_text="Viviendas pendientes de aprobación")
    organismo = models.ForeignKey(Organismo, help_text="Organismo que ocupa el local", related_name="locales_org", on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, auto_created=True, help_text="Fecha en que se introdujo el local al sistema.")
    acta = models.CharField(max_length=9, verbose_name="Acta", validators=[validate_acta_acuerdo])
    acuerdoCAM = models.CharField(max_length=9, verbose_name="Acuerdo CAM", validators=[validate_acta_acuerdo])
    acuerdoPEM = models.CharField(max_length=9, verbose_name="Acuerdo PEM", validators=[validate_acta_acuerdo])
    acuerdoORG = models.CharField(max_length=9, verbose_name="Acuerdo Organismo", validators=[validate_acta_acuerdo])
    observaciones = models.TextField(max_length=600, verbose_name="Otras observaciones")
    estatal = models.BooleanField(default=True, verbose_name="Es estatal")
    no_expediente = models.PositiveSmallIntegerField(verbose_name="No. Expediente", unique=True)

    class Meta:
        verbose_name = "Local"
        ordering = ['fecha', ]
        verbose_name_plural = "Locales"
        unique_together = (('municipio', 'direccion_calle', 'direccion_numero', 'piso', ),)

    def __str__(self):
        return self.municipio.nombre + '-' + self.direccion_calle.nombre + '-' + self.direccion_numero

