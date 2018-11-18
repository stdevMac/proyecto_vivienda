from django import forms
from django.contrib.auth.validators import *
from django.core.validators import MinLengthValidator, MaxLengthValidator

from apps.dpv_nomencladores.models import Genero, Calle
from apps.dpv_nomencladores.validators import only_letters, only_numbers
from .models import *
from apps.dpv_persona.models import PersonaJuridica, PersonaNatural

# class ComplaintForm(forms.Form):
#     stat = {
#         ('P', 'Pendiente'),
#         ('EA', 'Esperando Asignacion'),
#         ('ERT', 'Esperando Respuesta de Tecnico'),
#         ('EAJ', 'Esperando aceptacion del jefe'),
#     }
#     procedency = forms.CharField(max_length=50, label="Procedencia")  # models.CharField(max_length=50,label="Procedencia de la Queja")
#     body = forms.CharField(max_length=1000, label="Cuerpo de la Queja", widget=forms.Textarea)
#     topic = forms.CharField(max_length=200, label="Titulo de la Queja")
#     number = forms.CharField(max_length=15, label="Numero de la Queja")
#     status = forms.ChoiceField(choices=stat, label="Estado de la Queja")

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        exclude = ('enterDate', 'is_natural', 'person_juridic', 'person_natural')
            # 'enterDate = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Introduccion de la Queja")
    # is_natural = models.BooleanField(verbose_name="Es Natural",default=True)
    # person_natural = models.ForeignKey(PersonaNatural, null=True, on_delete=models.CASCADE, verbose_name="Persona Natural  que Presenta la Queja", blank=True)
    # person_juridic'

class WaitingForDistributionForm(ComplaintForm):
    pass

class TecnicForm(forms.ModelForm):
    class Meta:
        model = Tecnic
        fields = '__all__'

class AsignedToTecnicForm(forms.ModelForm):
    class Meta:
        model = AsignedToTecnic
        exclude = (
            'enterDate',
            'complaint',
        )


class FinishedComplaintForm(forms.ModelForm):
    class Meta:
        model = FinishedComplaint
        exclude = (
            'enterDate',
            'complaint',
        )


class AcceptedForm(forms.ModelForm):
    class Meta:
        model = Accepted
        exclude = (
            'finishedDate',
            'complaint',
            'bossAccepted',
            'tecnicWorkInComplaint',
        )
