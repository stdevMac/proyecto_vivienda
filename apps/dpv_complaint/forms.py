from django import forms
from django.contrib.auth.validators import *
from django.core.validators import MinLengthValidator, MaxLengthValidator

from apps.dpv_nomencladores.models import Genero, Calle
from apps.dpv_nomencladores.validators import only_letters, only_numbers
from .models import *
from apps.dpv_persona.models import PersonaJuridica, PersonaNatural

class ComplaintForm(forms.Form):
    procedency = forms.CharField(max_length=50, label="Procedencia")  # models.CharField(max_length=50,label="Procedencia de la Queja")
    body = forms.CharField(max_length=1000, label="Cuerpo de la Queja", widget=forms.Textarea)
    topic = forms.CharField(max_length=200, label="Titulo de la Queja")
    number = forms.CharField(max_length=15, label="Numero de la Queja")
    status = forms.CharField(max_length=15, label="Estado de la Queja")

class WaitingForDistributionForm(ComplaintForm):
    pass


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
