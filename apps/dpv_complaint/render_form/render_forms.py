from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.dpv_complaint.forms import *
from apps.dpv_complaint.models import *
from apps.dpv_persona.forms import PersonaNaturalForm, PersonaJuridicaForm


def form_NaturalComplaint(request):
    _form_name = "Queja de persona Natural"
    if request.method == "POST":
        _form_complaint = ComplaintForm(request.POST)
        _form_natural = PersonaNaturalForm(request.POST)
        if _form_complaint.is_valid() and _form_natural.is_valid():

            complaint = _form_complaint.save(commit=False)
            complaint.is_natural = True
            complaint.person_natural = _form_natural.save()
            complaint.enterDate = timezone.now()
            complaint.save()
            p = WaitingForDistribution()
            p.complaint = complaint
            p.enterDate = timezone.now()
            p.save()
            return redirect(reverse_lazy('index_natural_complaint'))
    else:
        _form_complaint = ComplaintForm()
        _form_natural = PersonaNaturalForm()
    return render(request, "dpv_complaint/multiform_complaint.html", {'form_one': _form_complaint, 'form_two': _form_natural, 'form_name': _form_name})


def form_JuridicComplaint(request):
    _form_name = "Queja de persona Juridica"
    if request.method == "POST":
        _form_complaint = ComplaintForm(request.POST)
        _form_juridic = PersonaJuridicaForm(request.POST)
        if _form_complaint.is_valid() and _form_juridic.is_valid():
            complaint = _form_complaint.save(commit=False)
            complaint.is_natural = False
            complaint.person_natural = _form_juridic.save()
            complaint.enterDate = timezone.now()
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


def form_FinishedComplaint(request):
    _form_name = "Queja por Para Responder"
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
    return render(request, "dpv_complaint/single_form.html", {'form':_form, 'form_name': _form_name})


def form_Accepted(request, finished_id):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AcceptedForm(request.POST)
        if _form.is_valid():
            finished = FinishedComplaint.objects.get(id=finished_id)
            _post = _form.save(commit = False)
            _post.finishedDate = timezone.now()
            _post.complaint = finished.complaint
            _post.tecnicWorkInComplaint = finished.tecnic
            _post.argumentsOfTecnic = finished.arguments
            _post.bossAccepted = request.user.id
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy('index_accepted'))
    else:
        _form = FinishedComplaintForm()
    return render(request, "", {'form':_form, 'form_name': _form_name})


def form_AsignDepartment(request, complaint_id):
    _form_name = "Asignar Departamento"
    if request.method == 'POST':
        _form = AsignDepartmentForm(request.POST)
        if _form.is_valid():
            args = _form.fields['department']._queryset.first()
            Complaint.objects.filter(id=complaint_id).update(department=args)
            return redirect(reverse_lazy('index_natural_complaint'))
    else:
        _form = AsignDepartmentForm()
    return render(request, 'dpv_complaint/single_form.html',{ 'form' : _form, 'form_name' : _form_name })

