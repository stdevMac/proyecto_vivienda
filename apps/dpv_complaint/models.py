from django.db import models
from apps.dpv_nomencladores.models import AreaTrabajo
from apps.dpv_perfil.models import Perfil
from django.utils import timezone
from apps.dpv_persona.models import *

stat = {
    ('Pendiente', 'P'),
    ('Esperando Asignacion', 'EA'),
    ('Esperando Respuesta de Tecnico', 'ERT'),
    ('Esperando aceptacion del jefe', 'EAJ'),
}
ans = {
    ('S', "Solucion o Resuelto"),
    ('PS', 'Pendiente de Solucion'),
    ('PR', 'Pendiente de Respuesta'),
    ('ECNS', 'Explicada Causa de no Solucion'),
    ('Tramite', 'Tramite')
}


class Complaint(models.Model):
    origin = models.CharField(max_length=50, )
    body = models.CharField(max_length=1000, )
    topic = models.CharField(max_length=200, )
    number = models.CharField(max_length=15,)
    status = models.CharField(choices=stat, default='Pendiente', max_length=20, )
    enter_date = models.DateTimeField(default=timezone.now, )
    is_natural = models.BooleanField(default=True)
    person_natural = models.ForeignKey(PersonaNatural, related_name='person_natural', on_delete=False, blank=True)
    person_juridic = models.ForeignKey(PersonaJuridica, related_name='person_juridic', on_delete=models.CASCADE, blank=True)
    department = models.ForeignKey(AreaTrabajo, related_name='department', on_delete=False, null=True)


class Technical(models.Model):
    profile = models.ForeignKey(Perfil, on_delete=False, related_name='profile')


class Documents(models.Model):
    text = models.TextField()


class WaitingForDistribution(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=False)
    enter_date = models.DateTimeField(default=timezone.now, )


class AssignedToTechnician(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=False, )
    technical = models.ForeignKey(Technical, on_delete=models.CASCADE,)
    enter_date = models.DateTimeField(default=timezone.now, )


class FinishedComplaint(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=False,)
    technical = models.ForeignKey(Technical, on_delete=False,)
    technical_args = models.ForeignKey(Documents, on_delete=False, related_name='technical_args')
    enter_date = models.DateTimeField(default=timezone.now)


class Accepted(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=False,)
    technical_work_in_complaint = models.ForeignKey(Technical, on_delete=False, default=1,
                                                    related_name='technical_accepted')
    technical_args = models.ForeignKey(Documents, on_delete=False, related_name='technical_args_accepted')
    final_args = models.ForeignKey(Documents, False)
    finished_date = models.DateTimeField(default=timezone.now)
    boss_accepted = models.ForeignKey(Perfil, on_delete=False, default=False, related_name='boss_accepted')
    answer = models.CharField(choices=ans, default='S', max_length=100, )


class HistoryComplaint(models.Model):
    complaint = models.ForeignKey(Complaint,  on_delete=False, )
    technical = models.ForeignKey(Technical, on_delete=False, related_name='technical_history', blank=True)
    boss = models.ForeignKey(Perfil, on_delete=False, blank=True)
    state = models.CharField(choices=stat, default='Pendiente', max_length=200)
    technical_args = models.ForeignKey(Documents, related_name='technical_args_history', on_delete=False, blank=True)
    boss_args = models.ForeignKey(Documents, on_delete=False, related_name='boss_args_history', blank=True)
    boss_answer = models.CharField(choices=ans, default='S', max_length=20, blank=False)
    date_of_status = models.DateTimeField(auto_now_add=True)
