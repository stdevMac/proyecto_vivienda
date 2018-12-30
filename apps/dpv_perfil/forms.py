from django import forms
from django.contrib.auth.models import User
from .models import Perfil
from apps.dpv_persona.models import Persona


# Put your Forms Here
class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('notificacion_email', 'documentacion_email', 'avatar', 'centro_trabajo', 'depto_trabajo', )


class PerfilMForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('notificacion_email', 'documentacion_email', 'centro_trabajo', 'depto_trabajo',  'datos_usuario', 'datos_personales', )

        widgets = {
            'notificacion_email': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'documentacion_email': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'centro_trabajo': forms.Select(attrs={"placeholder": "Seleccione una Unidad.", "class": "form-control"}),
            'depto_trabajo': forms.Select(attrs={"placeholder": "Seleccione un Departamento.", "class": "form-control"}),
            'datos_usuario': forms.Select(attrs={"hidden": "", "class": "noshow"}),
            'datos_personales': forms.Select(attrs={"hidden": "", "class": "noshow"}),
        }

