from django.db import models

# Create your models here.
from apps.dpv_nomencladores.models import AreaTrabajo
from apps.dpv_perfil.models import Perfil
from apps.dpv_persona.models import *

#generic complaint
class Complaint(models.Model):
    _procedency = models.CharField(max_length=50,verbose_name="Procedencia de la Queja")
    _body = models.CharField(max_length=1000,verbose_name="Cuerpo de la Queja")
    _topic = models.CharField(max_length=200,verbose_name="Titulo de la Queja")
    _number = models.CharField(max_length=15,verbose_name="Numero de la Queja")
    _status = models.CharField(max_length=15,verbose_name="Estado de la Queja")
    _enterDate = models.DateTimeField(verbose_name="Fecha de Introduccion de la Queja")
    _is = models.BooleanField(verbose_name="",default=True)


#employer in charge of analyzing the complaint
class Tecnic(models.Model):
    _perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Perfil del Tecnico")
    _workingArea = models.ForeignKey(AreaTrabajo, on_delete=models.CASCADE,verbose_name="Area de trabajo del Tecnico")


#complaint waiting for distribution in the bussines
class PresentedComplaint(models.Model):
    _complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE,verbose_name="Queja")
    _person = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE,verbose_name="PersonaNatural  que Presenta la Queja")

#waiting for distribution in the working area
class WaitingForDistribution(models.Model):
    _complaint = models.ForeignKey(PresentedComplaint, on_delete=models.CASCADE, verbose_name="Queja")
    _enterDate = models.DateTimeField( verbose_name="Fecha insertada la queja por PersonaNatural  para esperar la distribucion")


#waiting for the tecniccian to give it an answer
class AsignedToTecnic(models.Model):
    _complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, verbose_name="Queja por PersonaNatural ")
    _tecnic = models.ForeignKey(Tecnic, on_delete=models.CASCADE, verbose_name="Tecnico asignado a la Queja ")
    _enterDate = models.DateTimeField('now')

#the tecniccian gave an answer
class FinishedComplaint(models.Model):
    _complaint = models.ForeignKey(PresentedComplaint,on_delete=False, verbose_name="Queja por PersonaNatural ")
    _tecnic = models.ManyToManyField(Tecnic, verbose_name="Tecnico que atendio la Queja ")#.ForeignKey(Tecnic, on_delete=models.CASCADE)
    _finishedDate = models.DateTimeField('now')

#the answer given by the tecniccian was accepted by the boss
class Accepted(models.Model):
    _complaint = models.ForeignKey(PresentedComplaint,on_delete=False, verbose_name="Queja por PersonaNatural ")
