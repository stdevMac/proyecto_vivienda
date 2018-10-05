from django.db import models


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

