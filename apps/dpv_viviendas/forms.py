from django import forms
from .models import Vivienda


class ViviendaForm(forms.ModelForm):

    class Meta:
        model = Vivienda
        fileds = ['numero',
                  'destino',
                  'cantidad_persona',
                  'propietario',
                  'fecha_propietario',
                  'concepto',
                  'aprobada',
                  'add_concepto', ]