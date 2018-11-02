from django import forms
from django.contrib.auth.models import User
from .models import Perfil
from apps.dpv_persona.models import Persona


# Put your Forms Here
class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('notificacion_email', 'documentacion_email')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'date_joined', 'groups',)


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('ci', 'municipio', 'direccion_calle', 'direccion_numero', 'direccion_entrecalle1', 'direccion_entrecalle2',
                  'telefono', 'movil', 'genero', )


class FullPerfilForm(forms.Form):

    class Meta:
        fields = ('username',
                  'ci',
                  'documentacion_email',
                  'nombre',
                  'apellidos',
                  'direccion_calle',
                  'direccion_numero',
                  'direccion_entrecalle1',
                  'direccion_entrecalle2',
                  'municipio',
                  'telefono',
                  'movil',
                  'genero',
                  'notificacion_email',
                  'documentacion_email', )

