from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from apps.nomencladores.models import Municipio, Calle
from apps.nomencladores.validators import only_letters, only_numbers


# Create your models here.
class CentroTrabajo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Centro de trabajo", unique=True, validators=[MaxLengthValidator(50)])
    numero = models.PositiveSmallIntegerField(verbose_name="Número", blank=True)
    oc = models.BooleanField(default=False, verbose_name="Oficina Central")
    municipio = models.ForeignKey(Municipio, related_name="ubicacion_work", on_delete=models.CASCADE, help_text="Municipio donde está ubicado el centro")

    class Meta:
        verbose_name = "Centro de Trabajo"
        verbose_name_plural = "Centro de Trabajo"
        ordering = ["numero", "nombre", ]

    def __str__(self):
        return self.nombre


class AreaTrabajo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Área de Trabajo", unique=True, validators=[MaxLengthValidator(50)])
    numero = models.CharField(max_length=3, blank=True, verbose_name="Número", validators=[MaxLengthValidator(3),
                                                                                           only_numbers])

    class Meta:
        verbose_name = "Área de Trabajo"
        verbose_name_plural = "Áreas de Trabajo"
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


class Persona(models.Model):
    nombre = models.CharField(max_length=30, validators=[MaxLengthValidator(30), only_letters])
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, verbose_name="Municipio", help_text="Municipio donde recide la persona")
    direccion_calle = models.ForeignKey(Calle, on_delete=models.CASCADE, verbose_name="Calle", blank=True)
    direccion_numero = models.PositiveSmallIntegerField(blank=True, verbose_name="Número")
    telefono = models.CharField(max_length=8, verbose_name="Teléfono Fijo", blank=True, validators=[MinLengthValidator(8),
                                                                                                    MaxLengthValidator(8),
                                                                                                    only_numbers])
    movil = models.CharField(max_length=8, verbose_name="Teléfono Movil", blank=True, unique=True, validators=[MinLengthValidator(8),
                                                                                                               MaxLengthValidator(8),
                                                                                                               only_numbers])
    email_address = models.EmailField(verbose_name="Correo Electrónico", blank=True, unique=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        abstract = True

    def __str__(self):
        return self.nombre


class PersonaNatural(Persona):
    apellidos = models.CharField(max_length=50, validators=[MaxLengthValidator(50), only_letters])
    ci = models.CharField(max_length=11, validators=[MinLengthValidator(11, message="Este campo no puede tener menos de 11 caracteres"),
                                                     MaxLengthValidator(11, message="Este campo no puede tener más de 11 caracteres"),
                                                     only_numbers], unique=True)
    direccion_entrecalle1 = models.ForeignKey(Calle, related_name="persona_entrecalle1", on_delete=models.CASCADE, verbose_name="Primera Entrecalle", blank=True)
    direccion_entrecalle2 = models.ForeignKey(Calle, related_name="persona_entrecalle2", on_delete=models.CASCADE, verbose_name="Segunda Entrecalle", blank=True)
    genero = models.ForeignKey(Genero, verbose_name="Género", blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Persona Natural"
        verbose_name_plural = "Personas Naturales"
        ordering = ["ci", "apellidos", ]

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)


class PersonaJuridica(Persona):
    codigo_nit = models.CharField(max_length=11)
    codigo_reuup = models.CharField(max_length=11)

    class Meta:
        verbose_name = "Persona Jurídica"
        verbose_name_plural = "Personas Jurídicas"