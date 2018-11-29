from django import forms
from .models import *

class ComplaintForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = AreaTrabajo.objects.all()

    class Meta:
        model = Complaint
        exclude = ('enterDate', 'is_natural', 'person_juridic', 'person_natural', 'status',)


class AsignDepartmentForm(forms.Form):
    department = forms.ModelChoiceField(queryset=AreaTrabajo.objects.all(), label='Seleccione Area de Trabajo')


class TecnicForm(forms.ModelForm):
    class Meta:
        model = Tecnic
        fields = '__all__'


class AsignedToTecnicForm(forms.ModelForm):
    class Meta:
        model = AsignedToTecnic
        exclude = ('enterDate', 'complaint',)


class FinishedComplaintForm(forms.ModelForm):
    class Meta:
        model = FinishedComplaint
        exclude = ('enterDate', 'tecnic', 'complaint',)


class AcceptedForm(forms.ModelForm):
    class Meta:
        model = Accepted
        exclude = ('finishedDate', 'complaint', 'bossAccepted', 'tecnicWorkInComplaint', 'argumentsOfTecnic')