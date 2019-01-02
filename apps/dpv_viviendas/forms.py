from django import forms
from .models import Vivienda


class ViviendaForm(forms.ModelForm):

    class Meta:
        model = Vivienda
        fields = ['numero',
                  'destino',
                  'cantidad_persona',
                  'propietario',
                  'fecha_propietario',
                  'concepto',
                  'aprobada',
                  'add_concepto', ]
        widgets = {
            'numero': forms.TextInput(attrs={"placeholder": "Número", "class": "form-control"}),
            'cantidad_persona': forms.TextInput(attrs={"placeholder": "Cantidad de Personas", "class": "form-control"}),
            'add_concepto': forms.Textarea(attrs={"placeholder": "Sobre concepto", "class": "form-control"}),
            'propietario': forms.Select(attrs={"placeholder": "Seleccione un Propietario.", "class": "form-control"}),
            'concepto': forms.Select(attrs={"placeholder": "Seleccione un Concepto.", "class": "form-control"}),
            'destino': forms.Select(attrs={"placeholder": "Seleccione un Destino.", "class": "form-control"}),
            'aprobada': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }