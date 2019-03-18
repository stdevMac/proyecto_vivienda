from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.dpv_complaint.forms import *
from apps.dpv_complaint.models import *
from apps.dpv_persona.forms import PersonaNaturalForm, PersonaJuridicaForm


def check_natural_person(ci, email_address):
    # Check if exist a person for the CI
    by_ci = PersonaNatural.objects.filter(ci=ci)
    by_email = PersonaNatural.objects.filter(email_address=email_address)
    return by_ci.exists() or by_email.exists()


def form_natural_complaint(request, person_id):
    form_name = "Datos de Queja Natural"
    if request.method == "POST":
        form_complaint = ComplaintForm(request.POST)
        if form_complaint.is_valid():

            complaint = form_complaint.save(commit=False)
            complaint.is_natural = True
            complaint.person_natural = PersonaNatural.objects.get(id=person_id)
            complaint.enter_date = timezone.now()
            complaint.save()
            p = WaitingForDistribution()
            p.complaint = complaint
            p.enterDate = timezone.now()
            p.save()
            return redirect(reverse_lazy('get_complaints_for_person', args=[person_id]))
    else:
        form_complaint = ComplaintForm()
    return render(request, "dpv_complaint/single_form.html",
                  {'form': form_complaint, 'form_name': form_name})


def middle_form_natural_complaint(request, person_id):
    complaints = Complaint.objects.all().filter(person_natural=person_id)
    if complaints.exists():
        return render(request, "dpv_complaint/index_by_person.html", {'index': complaints,
                                                                      'index_name': 'Obtener Persona por ID'})
    else:
        return redirect(reverse_lazy('add_natural_complaint', args=[person_id]))
    pass


def form_person_for_complaint(request):
    form_name = "Datos de persona Natural"
    if request.method == "POST":
        form_natural = PersonaNaturalForm(request.POST)
        email = form_natural.data.get('email_address')
        ci = form_natural, form_natural.data.get('ci')
        if check_natural_person(ci, email):
            if email:
                person = PersonaNatural.objects.get(email_address=email)
            else:
                person = PersonaNatural.objects.get(email_address=email)
            return redirect(reverse_lazy('get_complaints_for_person', args=[person.id]))

        elif form_natural.is_valid():
            person = form_natural.save()
            return redirect(reverse_lazy('add_natural_complaint', args=[person.id]))

    else:
        form_natural = PersonaNaturalForm()
    return render(request, "dpv_complaint/single_form.html",
                  {'form': form_natural, 'form_name': form_name})


def form_juridic_complaint(request):
    _form_name = "Queja de persona Juridica"
    if request.method == "POST":
        _form_complaint = ComplaintForm(request.POST)
        _form_juridic = PersonaJuridicaForm(request.POST)
        if _form_complaint.is_valid() and _form_juridic.is_valid():
            complaint = _form_complaint.save(commit=False)
            complaint.is_natural = False
            complaint.person_natural = _form_juridic.save()
            complaint.enter_date = timezone.now()
            complaint.department = None
            complaint.save()
            p = WaitingForDistribution()
            p.complaint = complaint
            p.enterDate = timezone.now()
            p.save()
            return redirect(reverse_lazy('index_juridic_complaint'))
    else:
        _form_complaint = ComplaintForm()
        _form_juridic = PersonaJuridicaForm()
    return render(request, "dpv_complaint/multiform_complaint.html", {'form_one':_form_complaint, 'form_two': _form_juridic, 'form_name': _form_name})


def form_finished_complaint(request):
    _form_name = "Queja por Responder"
    if request.method == "POST":
        _form = FinishedComplaintForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit = False)
            _post._enterDate = timezone.now()
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy(''))
    else:
        _form = FinishedComplaintForm()
    return render(request, "dpv_complaint/single_form.html", {'form': _form, 'form_name': _form_name})


def form_accepted(request, finished_id):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AcceptedForm(request.POST)
        if _form.is_valid():
            finished = FinishedComplaint.objects.get(id=finished_id)
            _post = _form.save(commit=False)
            _post.finished_date = timezone.now()
            _post.complaint = finished.complaint
            _post.technical_work_in_complaint = finished.technical
            _post.technical_args = finished.technical_args
            _post.bossAccepted = request.user.id
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy('index_accepted'))
    else:
        _form = FinishedComplaintForm()
    return render(request, "", {'form': _form, 'form_name': _form_name})


def form_assign_department(request, complaint_id):
    form_name = "Asignar Departamento"
    if request.method == 'POST':
        form = AssignDepartmentForm(request.POST)
        if form.is_valid():
            args = form.fields['department'].queryset.first()
            Complaint.objects.filter(id=complaint_id).update(department=args)
            return redirect(reverse_lazy('index_natural_complaint'))
    else:
        form = AssignDepartmentForm()
    return render(request, 'dpv_complaint/single_form.html', {'form': form, 'form_name': form_name})

