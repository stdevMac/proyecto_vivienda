from django import forms
from .models import PersonaNatural, PersonaJuridica


class PersonaNaturalForm(forms.ModelForm):

    class Meta:
        model = PersonaNatural
        fields = ('nombre',
                  'apellidos',
                  'ci',
                  'email_address',
                  'telefono',
                  'movil',
                  'direccion_calle',
                  'direccion_numero',
                  'direccion_entrecalle1',
                  'direccion_entrecalle2',
                  'municipio',
                  'genero', )


class PersonaJuridicaForm(forms.ModelForm):

    class Meta:
        model = PersonaJuridica
        fields = ('nombre',
                  'telefono',
                  'movil',
                  'email_address',
                  'direccion_calle',
                  'direccion_numero',
                  'direccion_entrecalle1',
                  'direccion_entrecalle2',
                  'municipio',
                  'codigo_nit',
                  'codigo_reuup', )