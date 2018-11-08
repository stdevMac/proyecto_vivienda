from django.db import models

# Create your models here.
from apps.dpv_nomencladores.models import AreaTrabajo
from apps.dpv_perfil.models import Perfil
from apps.dpv_persona.models import PersonaJuridica, PersonaNatural


class Complaint(models.Model):
    procedency = models.CharField(max_length=50,verbose_name="Procedencia de la Queja")
    body = models.CharField(max_length=1000,verbose_name="Cuerpo de la Queja")
    topic = models.CharField(max_length=200,verbose_name="Titulo de la Queja")
    number = models.CharField(max_length=15,verbose_name="Numero de la Queja")
    status = models.CharField(max_length=15,verbose_name="Estado de la Queja")
    enter_date = models.DateTimeField(verbose_name="Fecha de Introduccion de la Queja")


class Tecnic(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Perfil del Tecnico")
    working_area = models.ForeignKey(AreaTrabajo, on_delete=models.CASCADE,verbose_name="Area de trabajo del Tecnico")


class PresentedComplaintJuridic(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE,verbose_name="Queja")
    person = models.ForeignKey(PersonaJuridica, on_delete=models.CASCADE,verbose_name="Persona Juridica que Presenta la Queja")


class PresentedComplaintNatural(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE,verbose_name="Queja")
    person = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE,verbose_name="Persona Natural que Presenta la Queja")


class WaitingForDistributionNatural(models.Model):
    complaint = models.ForeignKey(PresentedComplaintNatural, on_delete=models.CASCADE, verbose_name="Queja")
    enter_date = models.DateTimeField( verbose_name="Fecha insertada la queja por persona natural para esperar la distribucion")


class WaitingForDistributionJuridic(models.Model):
    complaint = models.ForeignKey(PresentedComplaintJuridic, on_delete=models.CASCADE, verbose_name="Queja")
    enter_date = models.DateTimeField(verbose_name="Fecha insertada la queja por persona juridica para esperar la distribucion")


class AsignedToDepartmentNatural(models.Model):
    complaint = models.ForeignKey(PresentedComplaintNatural, on_delete=models.CASCADE)
    working_area = models.ForeignKey(AreaTrabajo, on_delete=models.CASCADE, verbose_name="Area de Trabajo asignada")
    enter_date = models.DateTimeField('now')


class AsignedToDepartmentJuridic(models.Model):
    complaint = models.ForeignKey(PresentedComplaintJuridic, on_delete=models.CASCADE)
    working_area = models.ForeignKey(AreaTrabajo, on_delete=models.CASCADE)
    enter_date = models.DateTimeField('now')


class AsignedToTecnicNatural(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, verbose_name="Queja por Persona Natural")
    tecnic = models.ForeignKey(Tecnic, on_delete=models.CASCADE, verbose_name="Tecnico asignado a la Queja Natural")
    enter_date = models.DateTimeField('now')

class AsignedToTecnicJuridic(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, verbose_name="Queja por Persona Juridica")
    tecnic = models.ManyToManyField(Tecnic, verbose_name="Tecnico asignado a la Queja Juridica")
    enter_date = models.DateTimeField('now')

class FinishedComplaintNatural(models.Model):
    complaint = models.ForeignKey(PresentedComplaintNatural,on_delete=False, verbose_name="Queja por Persona Natural")
    tecnic = models.ManyToManyField(Tecnic, verbose_name="Tecnico que atendio la Queja Natural")#.ForeignKey(Tecnic, on_delete=models.CASCADE)
    finished_date = models.DateTimeField('now')


class FinishedComplaintJuridic(models.Model):
    complaint = models.ForeignKey(PresentedComplaintJuridic,on_delete=False, verbose_name="Queja por Persona Juridica")
    tecnic = models.ManyToManyField(Tecnic, verbose_name="Tecnico que atendio la Queja Juridica")#.ForeignKey(Tecnic, on_delete=models.CASCADE)
    finished_date = models.DateTimeField('now')