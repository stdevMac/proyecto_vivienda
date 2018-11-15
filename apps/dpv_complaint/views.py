from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import *
from .models import *
from apps.dpv_persona.forms import *
from apps.dpv_persona.models import *

# Create your views here.

def form_Complaint(request):
    _form_name = "Queja"
    if request.method == "POST":
        _form = ComplaintForm(request.POST)
        if _form.is_valid():
            # _complaint = Complaint()#args
            # _post = _form.save(commit = False)
            # _post._enter_date = timezone.now()
            # _post.id = _post.pk
            # _post.save()
            return redirect(reverse_lazy('index_complaint'))
    else:
        _form = ComplaintForm()
    return render(request, "dpv_complaint/create_complaint.html", {'form':_form, 'form_name': _form_name})

def form_NaturalComplaint(request):
    _form_name = "Queja de persona Natural"
    if request.method == "POST":
        _form_complaint = ComplaintForm(request.POST)
        _form_natural = PersonaNaturalForm(request.POST)
        if _form_complaint.is_valid() or _form_natural.is_valid():
            _complaint = Complaint(_form_complaint) #args
            _person = PersonaNatural(_form_natural)
            _person.save()
            _complaint._is_natural = True
            _complaint._person_natural = _person
            _complaint._enterDate = timezone.now()
            _complaint.save()
            return redirect(reverse_lazy('index_complaint'))
    else:
        _form_complaint = ComplaintForm()
        _form_natural = PersonaNaturalForm()
    return render(request, "dpv_complaint/multiform_complaint.html", {'form_one':_form_complaint, 'form_two': _form_natural, 'form_name': _form_name})

#
# def form_PresentedComplaint(request):
#     _form_name = "Queja Presentada"
#     if request.method == "POST":
#         _form = PresentedComplaintForm(request.POST)
#         if _form.is_valid():
#             # _complaint = Complaint()revisar como crear las tablas persona y quejas
#             _post = _form.save(commit=False)
#             _post._enter_date = timezone.now()
#             _post.id = _post.pk
#             _post.save()
#             return redirect(reverse_lazy('index_presented_complaint'))and
#     else:
#         _form = PresentedComplaintForm()
#     return render(request, "dpv_complaint/create_complaint.html", {'form': _form,'form_name': _form_name})

def form_WaitingForDistribution(request):
    _form_name = "Quejas por distribuir"
    if request.method == "POST":
        _form = WaitingForDistributionForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit=False)
            _post._enter_date=timezone.now()
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy('index_WaitingForDistribution'))
    else:
        _form = WaitingForDistributionForm()
    return render(request, "dpv_complaint/create_complaint.html",{'form':_form, 'form_name': _form_name})

def form_AsignedToTecnic(request):
    _form_name = "Quejas en proceso de evaluacion"
    if request.method == "POST":
        _form = AsignedToTecnicForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit = False)
            _post._enter_date = timezone.now()
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy('index_asigned_to_tecnic'))
    else:
        _form = AsignedToTecnicForm()
    return render(request,"dpv_complaint/create_complaint.html", {'form':_form, 'form_name':_form_name})

def form_FinishedComplaint(request):
    _form_name = "Queja por revisar"
    if request.method == "POST":
        _form = FinishedComplaintForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit = False)
            _post._enter_date = timezone.now()
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy(''))
    else:
        _form = FinishedComplaintForm()
    return render(request, "dpv_complaint/create_complaint.html", {'form':_form, 'form_name': _form_name})

def form_Accepted(request):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AcceptedForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit = False)
            _post._enter_date = timezone.now()
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy())
    else:
        _form = FinishedComplaintForm()
    return render(request, "", {'form':_form, 'form_name': _form_name})

# Index
def index_Complaint(request):
    index_name = 'Indice de las Quejas'
    elems = Complaint.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", { 'index' : elems, 'index_name' : index_name })

def index_NaturalComplaint(request):
    index_name = 'Indice de las Quejas'
    elems = Complaint.objects.filter(_is_natural = True)
    return render(request, "dpv_complaint/index_complaint.html", {'index': elems, 'index_name': index_name})


def index_WaitingForDistribution(request):
    index_name = 'Indice de Quejas en espera de su distribucion'
    elems = WaitingForDistribution.objects.all()
    return render(request, "dpv_complaint/index_waiting_for_distribution.html", {'index': elems, 'index_name' : index_name })

def index_AsignedToTecnic(request):
    index_name = 'Quejas asignadas a los tecnicos'
    elems = AsignedToTecnic.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", {'index': elems, 'index_name' : index_name })

def index_FinishedComplaint(request):
    index_name = 'Indice de Quejas Finalizadas'
    elems = FinishedComplaint.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", { 'index' : elems, 'index_name' : index_name})

def index_Accepted(request):
    index_name = 'Indice de Quejas Aceptadas'
    elems = Accepted.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", { 'index' : elems, 'index_name' : index_name})


# Mov from state to state

def from_presentedComplaint_to_waitingForDistribution(request):
    pass

def from_waitingForDistribution_to_asignedToTecnic(request):
    pass

def from_asignedToTecnic_to_finishedComplaint(request):
    pass

def from_finishedComplaint_to_acceptedComplaint(request):
    pass

def from_finishedComplaint_to_reAsignedToTenic(request):
    pass

