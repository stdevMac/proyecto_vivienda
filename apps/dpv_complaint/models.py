from django.db import models
from apps.dpv_nomencladores.models import AreaTrabajo
from apps.dpv_perfil.models import Perfil
from django.utils import timezone
from apps.dpv_persona.models import *
from django.core.exceptions import ValidationError

#generic complaint
class Complaint(models.Model):
    stat = {
        ('Pendiente', 'P'),
        ('Esperando Asignacion', 'EA'),
        ('Esperando Respuesta de Tecnico', 'ERT'),
        ('Esperando aceptacion del jefe', 'EAJ'),
    }
    procedency = models.CharField(max_length=50,verbose_name="Procedencia de la Queja")
    body = models.CharField(max_length=1000,verbose_name="Cuerpo de la Queja")
    topic = models.CharField(max_length=200,verbose_name="Titulo de la Queja")
    number = models.CharField(max_length=15,verbose_name="Numero de la Queja")
    status = models.CharField(choices=stat, default='Pendiente', max_length=20,verbose_name="Estado de la Queja")
    enterDate = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Introduccion de la Queja")
    is_natural = models.BooleanField(verbose_name="Es Natural",default=True)
    person_natural = models.ForeignKey(PersonaNatural, null=True, on_delete=models.CASCADE, verbose_name="Persona Natural  que Presenta la Queja", blank=True)
    person_juridic = models.ForeignKey( PersonaJuridica, null=True, on_delete=models.CASCADE, verbose_name="Persona Juridica que Presenta la Queja", blank=True)
    department = models.ForeignKey(AreaTrabajo, on_delete=False, null=True)
    class Meta:
        verbose_name = "Queja"


#employer in charge of analyzing the complaint
class Tecnic(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Perfil del Tecnico")


#waiting for distribution in the working area
class WaitingForDistribution(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, verbose_name="Queja")
    enterDate = models.DateTimeField(default=timezone.now, verbose_name="Fecha insertada la queja por PersonaNatural  para esperar la distribucion")


#waiting for the tecniccian to give it an answer
class AsignedToTecnic(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, verbose_name="Queja por PersonaNatural ")
    tecnic = models.ForeignKey(Tecnic, on_delete=models.CASCADE, verbose_name="Tecnico asignado a la Queja ")
    enterDate = models.DateTimeField(default=timezone.now,verbose_name='Now')


#the tecniccian gave an answer
class FinishedComplaint(models.Model):
    complaint = models.ForeignKey(Complaint,on_delete=False, verbose_name="Queja por PersonaNatural ")
    tecnic = models.ForeignKey(Tecnic, on_delete=False,verbose_name="Tecnico que atendio la Queja ")#.ForeignKey(Tecnic, on_delete=models.CASCADE)
    arguments = models.CharField(default='', verbose_name="Respuesta del tecnico a la queja", max_length=1000)
    enterDate = models.DateTimeField(default=timezone.now, verbose_name='now')


#the answer given by the tecniccian was accepted by the boss
class Accepted(models.Model):
    complaint = models.ForeignKey(Complaint,on_delete=False, verbose_name="Queja por PersonaNatural ")
    tecnicWorkInComplaint = models.ForeignKey(Tecnic,on_delete=False,default=1, verbose_name="Tecnico que atendio la Queja ")
    argumentsOfTecnic = models.CharField(default='', verbose_name="Respuesta del tecnico a la queja", max_length=1000)
    finalArgumnets = models.CharField(default='', verbose_name="Respuesta final del jefe a la queja", max_length=1000)
    finishedDate = models.DateTimeField(default=timezone.now, verbose_name='now')
    bossAccepted = models.ForeignKey(Perfil, on_delete=False, default=False)
    ans = {
        ('S', 'Solucion o Resuelto'), # Solucion o Resuelto
        ('PS', 'Pendiente de Solucion'), # Pendiente de Solucion
        ('PR', 'Pendiente de Respuesta'), # Pendiente de Respuesta
        ('ECNS', 'Explicada Causa de no Solucion'), # Explicada Causa de no Solucion
        ('Tramite', 'Tramite') # Tramite
    }
    answer = models.CharField(choices=ans, default='S',max_length=100, verbose_name='Actual Respuesta de la queja', )