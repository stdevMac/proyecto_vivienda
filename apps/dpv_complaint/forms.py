import datetime

from django import forms
from .models import *


class ComplaintForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Complaint
        exclude = ('enter_date', 'is_natural', 'person_juridic', 'person_natural', 'status',
                   'anonymous', 'expiration_time', "department")


class AssignDepartmentForm(forms.Form):
    department = forms.ModelChoiceField(queryset=AreaTrabajo.objects.all(), label='Seleccione área de trabajo')


class TechnicianForm(forms.Form):
    technical = forms.ModelChoiceField(queryset=Technical.objects.all(), label='Disponibles')


class FinishedComplaintForm(forms.ModelForm):
    class Meta:
        model = FinishedComplaint
        exclude = ('enter_date', 'technical', 'complaint',)


class AcceptedForm(forms.ModelForm):
    class Meta:
        model = Accepted
        exclude = ('finished_date', 'complaint', 'boss_accepted', 'technical_work_in_complaint', 'technical_args')
        labels = {'final_args': 'Argumentos Finales', 'answer': 'Respuesta'}


stat_history = {
    ('', '--------'),
    ('Pendiente', 'Pendiente'),
    ('Esperando Asignación', 'Esperando Asignación'),
    ('Esperando Respuesta de Técnico', 'Esperando Respuesta de Técnico'),
    ('Esperando aceptación del jefe', 'Esperando aceptación del jefe'),
    ('Finalizada', 'Finalizada'),
}

CHOICES = (
    (None, "Todas"),
    (True, "Naturales"),
    (False, "Jurídicas")
)


class FilterForm(forms.Form):
    initial_time = forms.DateField(widget=forms.SelectDateWidget(), required=False,
                                   label='Inicio del rango')
    final_time = forms.DateField(widget=forms.SelectDateWidget(),
                                 initial=timezone.now(),
                                 required=False,
                                 label='Final del rango')
    municipality = forms.ModelChoiceField(queryset=Municipio.objects.all(), required=False, label='Municipio')
    status = forms.ChoiceField(choices=stat_history, required=False, initial='', label='Estado')
    natural = forms.ChoiceField(initial='Todas', choices=CHOICES,
                                label='Tipo de Quejas', required=False)
    department = forms.ModelChoiceField(queryset=AreaTrabajo.objects.all(), label='Departamento', required=False)

    def clean(self):
        cleaned_data = super(FilterForm, self).clean()
        initial_time = cleaned_data.get('initial_time')
        final_time = cleaned_data.get('final_time')

        if final_time and final_time > datetime.date.today():
            raise forms.ValidationError("La fecha final debe ser antes del día de hoy")

        if initial_time and initial_time > final_time:
            raise forms.ValidationError("La fecha inicial debe ser antes de la fecha final")

        return cleaned_data
