from django import forms
from .models import *


class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia

        fields = ['nombre', 'numero']

    def __init__(self, *args, **kwargs):
        super(ProvinciaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['numero', 'nombre', 'provincia']

        widgets = {
            'provincia': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        super(MunicipioForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class OrganismoForm(forms.ModelForm):
    class Meta:
        model = Organismo

        fields = ['nombre', 'siglas']

    def __init__(self, *args, **kwargs):
        super(OrganismoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class DestinoForm(forms.ModelForm):
    class Meta:
        model= Destino

        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(DestinoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class CalleForm(forms.ModelForm):
    class Meta:
        model= Calle

        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(CalleForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class PisoForm(forms.ModelForm):
    class Meta:
        model= Piso

        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(PisoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ConceptoForm(forms.ModelForm):
    class Meta:
        model= Concepto

        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(ConceptoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class GeneroForm(forms.ModelForm):
    class Meta:
        model= Genero

        fields = ['nombre', 'sigla']

    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class CentroTrabajoForm(forms.ModelForm):

    class Meta:
        model = CentroTrabajo
        fields = ['nombre', 'numero', 'siglas', 'municipio', 'oc']

        widgets = {
            'municipio': forms.Select(),
            'oc': forms.CheckboxInput()
        }

    def __init__(self, *args, **kwargs):
        super(CentroTrabajoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class AreaTrabajoForm(forms.ModelForm):

    class Meta:
        model = AreaTrabajo
        fields = ['nombre', 'numero', ]

    def __init__(self, *args, **kwargs):
        super(AreaTrabajoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })