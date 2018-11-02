from django import forms
from .models import Local


class LocalForm(forms.ModelForm):

    class Meta:
        model = Local
        fields = ['direccion_calle',
                  'direccion_numero',
                  'piso',
                  'direccion_entre1',
                  'direccion_entre2',
                  'municipio',
                  'no_viviendas',
                  'aprobado',
                  'pendiente',
                  'organismo',
                  'acta',
                  'acuerdoCAM',
                  'acuerdoPEM',
                  'acuerdoORG',
                  'acuerdo_DPV',
                  'estatal',
                  'observaciones', ]

