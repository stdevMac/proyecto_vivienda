from django import forms
from .models import *

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        exclude = ('enterDate', 'is_natural', 'person_juridic', 'person_natural', 'status',)
    def __init__(self):
        super(ComplaintForm, self).__init__()
        self.fields['department'].queryset = AreaTrabajo.objects.all()


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
        exclude = ('enterDate', 'complaint',)


class AcceptedForm(forms.ModelForm):
    class Meta:
        model = Accepted
        exclude = ('finishedDate', 'complaint', 'bossAccepted', 'tecnicWorkInComplaint',)