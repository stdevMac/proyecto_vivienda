from apps.dpv_nomencladores.models import AreaTrabajo
from apps.dpv_perfil.models import Perfil
from django.utils import timezone
from apps.dpv_persona.models import *

stat = {
    ('Pendiente', 'P'),
    ('Esperando Asignacion', 'EA'),
    ('Esperando Respuesta de Tecnico', 'ERT'),
    ('Esperando aceptacion del jefe', 'EAJ'),
    ('Finalizada', 'F'),
}
ans = {
    ('S', "Solucion o Resuelto"),
    ('PS', 'Pendiente de Solucion'),
    ('PR', 'Pendiente de Respuesta'),
    ('ECNS', 'Explicada Causa de no Solucion'),
    ('Tramite', 'Tramite')
}


class Complaint(models.Model):
    origin = models.CharField(max_length=50, verbose_name='Origen')
    body = models.CharField(max_length=1000, verbose_name='Cuerpo')
    topic = models.CharField(max_length=200, verbose_name='Titulo')
    number = models.CharField(max_length=15, verbose_name='Numero')
    status = models.CharField(choices=stat, default='Pendiente', max_length=20, )
    enter_date = models.DateTimeField(default=timezone.now, )
    is_natural = models.BooleanField(default=True)
    person_natural = models.ForeignKey(PersonaNatural, related_name='person_natural', on_delete=False,
                                       blank=True, null=True)
    person_juridic = models.ForeignKey(PersonaJuridica, related_name='person_juridic', on_delete=models.CASCADE,
                                       blank=True, null=True)
    department = models.ForeignKey(AreaTrabajo, related_name='department', on_delete=False, null=True, verbose_name='Departamento')
    anonymous = models.BooleanField(default=False)
    expiration_time = models.IntegerField(default=60)


class ConsejoPopular(models.Model):
    nombre = models.CharField(max_length=50)


class Approach(models.Model):
    reference_number = models.IntegerField()
    municipality = models.ForeignKey(Municipio, on_delete=False)
    popular_council = models.ForeignKey(ConsejoPopular, on_delete=False)
    entity = models.ForeignKey(PersonaJuridica, on_delete=False)
    topic = models.CharField(max_length=200, verbose_name='Titulo')
    text = models.CharField(max_length=1000)
    made_by = models.ForeignKey(PersonaNatural, related_name='approach_made_by', on_delete=False, blank=True)
    expiration_time = models.IntegerField(default=30)
    # address of the one how make the approach


class Technical(models.Model):
    profile = models.ForeignKey(Perfil, on_delete=False, related_name='profile')


class Documents(models.Model):
    text = models.TextField()


class WaitingForDistribution(models.Model):
    complaint = models.ForeignKey(Complaint, unique=True, on_delete=False)
    enter_date = models.DateTimeField(default=timezone.now, )


class AssignedToTechnician(models.Model):
    complaint = models.ForeignKey(Complaint, unique=True, on_delete=False, )
    technical = models.ForeignKey(Technical, on_delete=models.CASCADE,)
    enter_date = models.DateTimeField(default=timezone.now, )


class FinishedComplaint(models.Model):
    complaint = models.ForeignKey(Complaint, unique=True, on_delete=False,)
    technical = models.ForeignKey(Technical, on_delete=False,)
    technical_args = models.TextField()
    enter_date = models.DateTimeField(default=timezone.now)


class Accepted(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=False, unique=True, )
    technical_work_in_complaint = models.ForeignKey(Technical, on_delete=False, default=1,
                                                    related_name='technical_accepted')
    technical_args = models.TextField()
    final_args = models.TextField()
    finished_date = models.DateTimeField(default=timezone.now)
    boss_accepted = models.ForeignKey(Perfil, on_delete=False, default=False, related_name='boss_accepted')
    answer = models.CharField(choices=ans, default='S', max_length=100, )


class HistoryComplaint(models.Model):
    complaint = models.ForeignKey(Complaint,  on_delete=False, )
    technical = models.ForeignKey(Technical, on_delete=False, related_name='technical_history', blank=True)
    boss = models.ForeignKey(Perfil, on_delete=False, blank=True)
    state = models.CharField(choices=stat, default='Pendiente', max_length=200)
    technical_args = models.TextField()
    boss_args = models.TextField()
    boss_answer = models.CharField(choices=ans, default='S', max_length=20, blank=False)
    date_of_status = models.DateTimeField(auto_now_add=True)
    current_status = models.CharField(default='Pendiente', choices=stat, max_length=20)