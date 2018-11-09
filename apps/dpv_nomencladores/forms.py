from django import forms
from . import models


class MunicipioForm(forms.ModelForm):

    class Meta:
        model = models.Municipio
        fields = ('nombre',
                  'numero',
                  'provincia', )


class ProvinciaForm(forms.ModelForm):

    class Meta:
        model = models.Provincia
        fields = ('nombre',
                  'nombre', )


class OrganismoForm(forms.ModelForm):

    class Meta:
        model = models.Organismo
        fields = ('nombre',
                  'siglas', )


class DestinoForm(forms.ModelForm):

    class Meta:
        model = models.Destino
        fields = ('nombre', )


class CalleForm(forms.ModelForm):

    class Meta:
        model = models.Calle
        fields = ('nombre', )


class PisoForm(forms.ModelForm):

    class Meta:
        model = models.Piso
        fields = ('nombre', )


class CentroTrabajoForm(forms.ModelForm):

    class Meta:
        model = models.CentroTrabajo
        fields = ('nombre',
                  'siglas',
                  'numero',
                  'oc',
                  'municipio', )


class AreaTrabajoForm(forms.ModelForm):

    class Meta:
        model = models.AreaTrabajo
        fields = ('nombre',
                  'numero', )


class GeneroForm(forms.ModelForm):

    class Meta:
        model = models.Genero
        fields = ('nombre',
                  'sigla', )


class ConceptoForm(forms.ModelForm):

    class Meta:
        model = models.Concepto
        fields = ('nombre', )