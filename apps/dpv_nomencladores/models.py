from django.db import models
from .validators import only_numbers, only_letters
from django.core.validators import MaxLengthValidator, MinLengthValidator


# Create your models here.
class Provincia(models.Model):
    nombre = models.CharField(max_length=30, help_text="Nombre del municipio", verbose_name="Provincia", unique=True)
    numero = models.PositiveSmallIntegerField(verbose_name="Número", unique=True)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ["numero", ]

    def __str__(self):
        return  self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=30, help_text="Nombre del municipio", verbose_name="Municipio", unique=True)
    numero = models.PositiveSmallIntegerField(verbose_name="Número", unique=True)
    provincia = models.ForeignKey(Provincia, related_name="municipios", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ['numero', ]

    def __str__(self):
        return self.nombre


class Organismo(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre del organismo.", verbose_name=" Organismo", unique=True)
    siglas = models.CharField(max_length=7, help_text="Siglas representativas del organismo", unique=True)

    class Meta:
        verbose_name = "Organismo"
        verbose_name_plural = "Organismos"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre


class Destino(models.Model):
    nombre = models.CharField(max_length=50, help_text="Identificador del destino", verbose_name="Destino", unique=True)

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre


class Calle(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre de la calle", verbose_name="Calle", unique=True)

    class Meta:
        verbose_name = "Calle"
        verbose_name_plural = "Calles"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre


class Piso(models.Model):
    nombre = models.CharField(max_length=15, help_text="Nombre del piso", verbose_name="Piso", unique=True)

    class Meta:
        verbose_name = "Piso"
        verbose_name_plural = "Pisos"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre


class CentroTrabajo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Centro de trabajo", unique=True, validators=[MaxLengthValidator(50)], help_text="Nombre de la unidad.")
    siplas = models.CharField(max_length=5, verbose_name="Siglas", validators=[MaxLengthValidator(5)], help_text="Siglas de la entidad.")
    numero = models.PositiveSmallIntegerField(verbose_name="Número", blank=True, help_text="Número de la unidad")
    oc = models.BooleanField(default=False, verbose_name="Oficina Central", help_text="Indica si la unidad es la oficina central")
    municipio = models.ForeignKey(Municipio, related_name="ubicacion_work", on_delete=models.CASCADE, help_text="Municipio donde está ubicado el centro.")

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
        ordering = ["numero", "nombre", ]

    def __str__(self):
        return self.nombre


class AreaTrabajo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Área de Trabajo", unique=True, validators=[MaxLengthValidator(50)])
    numero = models.CharField(max_length=3, blank=True, verbose_name="Número", validators=[MaxLengthValidator(3),
                                                                                           only_numbers])

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ["nombre", ]

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=9, verbose_name="Género", unique=True, validators=[MaxLengthValidator(9),
                                                                                            only_letters])
    sigla = models.CharField(max_length=1, verbose_name="Inicial", unique=True, validators=[MinLengthValidator(1),
                                                                                            MaxLengthValidator(1),
                                                                                            only_letters])

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ['nombre', ]

    def __str__(self):
        return self.nombre


