from typing import Dict

from django import forms
from django.forms import TextInput

from .models import *


class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia

        fields = ['nombre', 'numero']

        widgets = {
<<<<<<< HEAD
            'nombre' : forms.TextInput(attrs={'placeholder':'Nombre', 'class': 'form-control malpha'}),
=======
            'nombre' : forms.TextInput(attrs={'placeholder':'Nombre', 'class': 'form-control mname'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
            'numero' : forms.TextInput(attrs={'placeholder':'Número', 'class': 'form-control mnumber'}),
        }


class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['numero', 'nombre', 'provincia']

        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control malpha'}),
=======
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control mnum'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
            'numero': forms.TextInput(attrs={'placeholder': 'Número', 'class': 'form-control mnumber'}),
            'provincia': forms.Select(attrs={'placeholder':'Seleccionar Provincia', 'class': 'form-control'})
        }

<<<<<<< HEAD
class ConsejoPopularForm(forms.ModelForm):
    class Meta:
        model = ConsejoPopular
        fields = ['numero', 'nombre', 'municipio']

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control malpha'}),
            'numero': forms.TextInput(attrs={'placeholder': 'Número', 'class': 'form-control mnumber'}),
            'municipio': forms.Select(attrs={'placeholder':'Seleccionar Municipio', 'class': 'form-control'})
        }

=======
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
class OrganismoForm(forms.ModelForm):
    class Meta:
        model = Organismo

        fields = ['nombre', 'siglas']

        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control malpha'}),
=======
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control mnum'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
            'siglas': forms.TextInput(attrs={'placeholder': 'Siglas', 'class': 'form-control mnum'}),
        }

class DestinoForm(forms.ModelForm):
    class Meta:
        model= Destino

        fields = ['nombre']

        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control malpha'}),
=======
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control mnum'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
        }

class CalleForm(forms.ModelForm):
    class Meta:
        model= Calle

        fields = ['nombre']

        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control malpha'}),
=======
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control mnum'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
        }

class PisoForm(forms.ModelForm):
    class Meta:
        model= Piso

        fields = ['nombre']

        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control malpha'}),
=======
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control mnum'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
        }

class ConceptoForm(forms.ModelForm):
    class Meta:
        model= Concepto

        fields = ['nombre']

        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control malpha'}),
=======
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control mname'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
        }


class GeneroForm(forms.ModelForm):
    class Meta:
        model= Genero

        fields = ['nombre', 'sigla']

        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs={'placeholder':'Nombre', 'class': 'form-control malpha'}),
            'sigla': forms.TextInput(attrs={'placeholder':'Sigla', 'class': 'form-control mnum'}),
=======
            'nombre': forms.TextInput(attrs={'placeholder':'Nombre', 'class': 'form-control mname'}),
            'sigla': forms.TextInput(attrs={'placeholder':'Sigla', 'class': 'form-control mname'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
        }

class CentroTrabajoForm(forms.ModelForm):

    class Meta:
        model = CentroTrabajo
        fields = ['nombre', 'numero', 'siglas', 'municipio', 'oc']

        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control malpha'}),
=======
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control mnum'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
            'numero': forms.TextInput(attrs={'placeholder': 'Número', 'class': 'form-control mnumber'}),
            'siglas': forms.TextInput(attrs={'placeholder': 'Siglas', 'class': 'form-control mnum'}),
            'municipio': forms.Select(attrs={'placeholder': 'Seleccionar Municipio', 'class': 'form-control'}),
            'oc': forms.CheckboxInput()
        }

class AreaTrabajoForm(forms.ModelForm):

    class Meta:
        model = AreaTrabajo

        fields = ['nombre', 'numero' ]

        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control malpha'}),
=======
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control mnum'}),
>>>>>>> 87b8f90f11e6b45efada971b42300c19b2a41ca1
            'numero': forms.TextInput(attrs={'placeholder': 'Número', 'class': 'form-control mnumber'}),
        }