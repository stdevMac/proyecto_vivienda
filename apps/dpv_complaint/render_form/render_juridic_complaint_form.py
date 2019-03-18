from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.dpv_complaint.forms import *
from apps.dpv_complaint.models import *
from apps.dpv_persona.forms import PersonaJuridicaForm


def form_juridic_complaint(request):
    form_name = "Queja de persona Juridica"
    if request.method == "POST":
        form_complaint = ComplaintForm(request.POST)
        form_juridic = PersonaJuridicaForm(request.POST)
        if form_complaint.is_valid() and form_juridic.is_valid():
            complaint = form_complaint.save(commit=False)
            complaint.is_natural = False
            complaint.person_natural = form_juridic.save()
            complaint.enter_date = timezone.now()
            complaint.department = None
            complaint.save()
            p = WaitingForDistribution()
            p.complaint = complaint
            p.enterDate = timezone.now()
            p.save()
            return redirect(reverse_lazy('index_juridic_complaint'))
    else:
        form_complaint = ComplaintForm()
        form_juridic = PersonaJuridicaForm()
    return render(request, "dpv_complaint/multiform_complaint.html",
                  {'form_one': form_complaint, 'form_two':
                      form_juridic, 'form_name': form_name})
