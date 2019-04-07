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


class AssignedToTechnicalForm(forms.ModelForm):
    class Meta:
        model = AssignedToTechnician
        exclude = ('enter_date', 'complaint', 'assigned_by')


class FinishedComplaintForm(forms.ModelForm):
    class Meta:
        model = FinishedComplaint
        exclude = ('enter_date', 'technical', 'complaint',)


class AcceptedForm(forms.ModelForm):
    class Meta:
        model = Accepted
        exclude = ('finished_date', 'complaint', 'boss_accepted', 'technical_work_in_complaint', 'technical_args')
        labels = {'final_args': 'Argumentos Finales', 'answer': 'Respuesta'}
