from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.dpv_complaint.forms import *
from apps.dpv_complaint.models import *
from apps.dpv_persona.forms import PersonaJuridicaForm


def check_juridic_person(codigo_nit, email_address):
    # Check if exist a person for the CI
    by_nit = PersonaJuridica.objects.filter(codigo_nit=codigo_nit)
    # Check if exist a person for the email
    by_email = PersonaJuridica.objects.filter(email_address=email_address)
    return by_nit.exists() or by_email.exists()


def form_juridic_complaint(request, juridic_id):
    form_name = "Queja de persona jurídica"
    if request.method == "POST":
        form_complaint = ComplaintForm(request.POST)
        person_juridic = PersonaJuridica.objects.get(id=juridic_id)
        if form_complaint.is_valid():
            complaint = form_complaint.save(commit=False)
            complaint.is_natural = False
            complaint.person_juridic = person_juridic
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
    return render(request, "dpv_complaint/form_complaint.html",
                  {'form': form_complaint, 'form_name': form_name})


def middle_form_juridic_complaint(request, juridic_id):
    complaints = Complaint.objects.all().filter(person_juridic=juridic_id)
    if complaints.exists():
        return render(request, "dpv_complaint/index_by_juridic.html", {'index': complaints,
                                                                       'index_name': 'Obtener persona por id'})
    else:
        return redirect(reverse_lazy('add_juridic_complaint', args=[juridic_id]))


def form_juridic_for_complaint(request):
    form_name = "Insertar persona jurídica"
    if request.method == "POST":
        form_juridic = PersonaJuridicaForm(request.POST)
        email = form_juridic.data.get('email_address')
        codigo_nit = form_juridic.data.get('codigo_nit')
        if check_juridic_person(codigo_nit, email):
            if email:
                person = PersonaNatural.objects.get(email_address=email)
            else:
                person = PersonaNatural.objects.get(codigo_nit=codigo_nit)
            return redirect(reverse_lazy('complaints_by_juridic', args=[person.id]))

        elif form_juridic.is_valid():
            person = form_juridic.save()
            return redirect(reverse_lazy('add_juridic_complaint', args=[person.id]))

    else:
        form_juridic = PersonaJuridicaForm()
    return render(request, "dpv_complaint/form_juridic_person.html",
                  {'form': form_juridic, 'form_name': form_name})
