from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from apps.dpv_nomencladores.models import Municipio, Organismo, Calle, Piso
from .validators import validate_acta_acuerdo, start_with_number


# Create your models here.
class Local(models.Model):
    direccion_calle = models.ForeignKey(Calle, related_name="calle_principal", help_text="Calle de la direccion", on_delete=models.CASCADE, verbose_name="Calle", blank=False, null=False)
    direccion_numero = models.CharField(max_length=10, help_text="Numero de la dirección", verbose_name="Número", validators=[start_with_number])
    piso = models.ForeignKey(Piso, help_text="Piso de la direccion del local", on_delete=models.CASCADE)
    direccion_entre1 = models.ForeignKey(Calle, related_name="entrecalle1", verbose_name="Primera Entrecalle", max_length=50, help_text="Primera entre calle de la dirección", on_delete=models.CASCADE)
    direccion_entre2 = models.ForeignKey(Calle, related_name="entrecalle2", verbose_name="Segunda Entrecalle", max_length=50, help_text="Segunda entre calle de la dirección", on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, related_name="locales_mun", help_text="Municipio donde se encuentra ubicado el local el local", on_delete="Null")
    no_viviendas = models.PositiveSmallIntegerField(verbose_name="Total de viviendas", help_text="Total de viviendas en el local", validators=[MaxValueValidator(50)])
    aprobado = models.BooleanField(default=False, help_text="Marque si está aprobado el local")
    pendiente = models.PositiveSmallIntegerField(verbose_name="Pendientes de aprobación", help_text="Viviendas pendientes de aprobación", validators=[MaxValueValidator(50)])
    organismo = models.ForeignKey(Organismo, help_text="Organismo que ocupa el local", related_name="locales_org", on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, auto_created=True, help_text="Fecha en que se introdujo el local al sistema.")
    acta = models.CharField(max_length=9, validators=[validate_acta_acuerdo], verbose_name="Acta")
    acuerdoCAM = models.CharField(max_length=9, verbose_name="Acuerdo CAM", validators=[validate_acta_acuerdo], blank=True, default='')
    acuerdoPEM = models.CharField(max_length=9, verbose_name="Acuerdo PEM", validators=[validate_acta_acuerdo], blank=True, default='')
    acuerdoORG = models.CharField(max_length=9, verbose_name="Acuerdo Organismo", validators=[validate_acta_acuerdo], blank=True, default='')
    observaciones = models.TextField(max_length=600, verbose_name="Otras observaciones")
    estatal = models.BooleanField(default=True, verbose_name="Es estatal")
    acuerdo_DPV = models.CharField(max_length=9, verbose_name="Acuerdo DPV",  validators=[validate_acta_acuerdo], default='', blank=True)
    data_ok = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    system_info = models.TextField(max_length=300, default='', blank=True)

    class Meta:
        verbose_name = "Local"
        ordering = ['fecha', ]
        verbose_name_plural = "Locales"
        unique_together = (('municipio', 'direccion_calle', 'direccion_numero', 'piso', ),)

    def __str__(self):
        return self.municipio.nombre + '-' + self.direccion_calle.nombre + '-' + self.direccion_numero

    def get_ok_data(self):
        validation_text = ''
        validation_point = 0

        if self.no_viviendas != Vivienda.objects.filter(local_dado=self).count():
            validation_point += 1
            validation_text += "No coincide el número de viviendas que es %d declarado en el local con el número de viviendas asociadas a el que es %d. \n" % (self.no_viviendas, Vivienda.objects.filter(local_dado=self).count())
        for viv in Vivienda.objects.filter(local_dado=self):
            pass