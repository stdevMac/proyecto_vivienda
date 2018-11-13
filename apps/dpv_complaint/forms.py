from django import forms
from django.contrib.auth.validators import *
from django.core.validators import MinLengthValidator, MaxLengthValidator

from apps.dpv_nomencladores.models import Genero, Calle
from apps.dpv_nomencladores.validators import only_letters, only_numbers
from .models import *
from apps.dpv_persona.models import PersonaJuridica, PersonaNatural

class ComplaintForm(forms.Form):
    _procedency = forms.CharField(max_length=50, label="Procedencia")  # models.CharField(max_length=50,label="Procedencia de la Queja")
    _body = forms.CharField(max_length=1000, label="Cuerpo de la Queja")
    _topic = forms.CharField(max_length=200, label="Titulo de la Queja")
    _number = forms.CharField(max_length=15, label="Numero de la Queja")
    _status = forms.CharField(max_length=15, label="Estado de la Queja")
    # def clean(self):
    #     if self._is_natural:
    #         if not self._person_natural or self._person_natural is '':
    #             raise ValidationError('En una queja natural tienque tener los datos de una perosna natural', code="not_natural_person")
    #     else:

class PresentedComplaintForm(forms.Form):
    _procedency = forms.CharField(max_length=50, label="Procedencia")#models.CharField(max_length=50,label="Procedencia de la Queja")
    _body = forms.CharField(max_length=1000,label="Cuerpo de la Queja")
    _topic = forms.CharField(max_length=200,label="Titulo de la Queja")
    _number = forms.CharField(max_length=15,label="Numero de la Queja")
    _status = forms.CharField(max_length=15,label="Estado de la Queja")
    _enterDate = forms.DateTimeField(label="Fecha de Introduccion de la Queja")
    # _is = forms.CharField(label="Juridica", widget=forms.BooleanField , )
    
    nombre = forms.CharField(max_length=30, validators=[MaxLengthValidator(30), only_letters])

    # municipio = forms.ForeignKey(Municipio, label="Municipio",
    #                               help_text="Municipio donde recide la persona")
    # direccion_calle = forms.ForeignKey(Calle, label="Calle", blank=True)
    # direccion_numero = forms.PositiveSmallIntegerField(blank=True, label="Número")
    telefono = forms.CharField(max_length=8, label="Teléfono Fijo",
                                validators=[MinLengthValidator(8),
                                            MaxLengthValidator(8),
                                            only_numbers])
    movil = forms.CharField(max_length=8, label="Teléfono Movil",
                             validators=[MinLengthValidator(8),
                                         MaxLengthValidator(8),
                                         only_numbers])
    email_address = forms.EmailField(label="Correo Electrónico")

    apellidos = forms.CharField(max_length=50, validators=[MaxLengthValidator(50), only_letters])
    ci = forms.CharField(max_length=11, validators=[
        MinLengthValidator(11, message="Este campo no puede tener menos de 11 caracteres"),
        MaxLengthValidator(11, message="Este campo no puede tener más de 11 caracteres"),
        only_numbers])
    # direccion_entrecalle1 = forms.ForeignKey(Calle, related_name="persona_entrecalle1",
    #                                           label="Primera Entrecalle", blank=True)
    # direccion_entrecalle2 = forms.ForeignKey(Calle, related_name="persona_entrecalle2",
    #                                           label="Segunda Entrecalle", blank=True)
    # genero = forms.ForeignKey(Genero, label="Género", blank=True)


class WaitingForDistributionForm(forms.Form):
    pass


class AsignedToTecnicForm(forms.Form):
    pass


class FinishedComplaintForm(forms.Form):
    pass


class AcceptedForm(models.Model):
    pass


# class PresentedComplaintNaturalForm(forms.Form):
#     complaint_procedency = forms.CharField(max_length=50,label='Procedencia de la queja', help_text='Esta es la ayuda')
#     complaint_topic = forms.CharField(max_length=200, label="Titulo")
#     complaint_body = forms.CharField(max_length=1000, label='Cuerpo',widget=forms.Textarea)
#     complaint_number = forms.CharField(max_length=15,label="Numero de la Queja")
#     complaint_status = forms.CharField(max_length=15,label="Estado de la Queja")
#
#     person_apellidos = forms.CharField(max_length=50, validators=[MaxLengthValidator(50), only_letters])
#     person_ci = forms.CharField(max_length=11, validators=[MinLengthValidator(11, message="Este campo no puede tener menos de 11 caracteres"),
#                                                      MaxLengthValidator(11, message="Este campo no puede tener más de 11 caracteres"),
#                                                      only_numbers])
#     calle_direccion_uno_nombre = forms.CharField(max_length=50, help_text="Nombre de la calle", label="Calle")
#     calle_direccion_dos_nombre = forms.CharField(max_length=50, help_text="Nombre de la calle", label="Calle")
#     genero_nombre = forms.CharField(max_length=9, label="Género", validators=[MaxLengthValidator(9),
#                                                                                             only_letters])
#     genero_sigla = forms.CharField(max_length=1, label="Inicial del Genero", validators=[MinLengthValidator(1),
#                                                                                             MaxLengthValidator(1),
#                                                                                             only_letters])
#
#
# class PresentedComplaintJuridicForm(forms.Form):
#     complaint_procedency = forms.CharField(max_length=50,label='Procedencia de la queja', help_text='Esta es la ayuda')
#     complaint_topic = forms.CharField(max_length=200, label="Titulo")
#     complaint_body = forms.CharField(max_length=1000, label='Cuerpo',widget=forms.Textarea)
#     complaint_number = forms.CharField(max_length=15,label="Numero de la Queja")
#     complaint_status = forms.CharField(max_length=15,label="Estado de la Queja")
