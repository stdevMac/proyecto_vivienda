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
    def __init__(self, *args, **kwargs):
        data = kwargs.pop('data')
        self.dept_id = data.pop('department_id')
        self.municipality_id = data.pop('municipality_id')
        super(TechnicianForm, self).__init__(*args, **kwargs)
        qs = Technical.objects.\
            filter(profile__centro_trabajo__municipio_id__exact=self.municipality_id, profile__depto_trabajo__department__exact=self.municipality_id)
        self.fields['technical'].queryset = qs

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
