from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import *
from .models import *
from apps.dpv_persona.forms import *
from apps.dpv_persona.models import *

# Create Forms
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
            # _form_natural.save()
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
    _form_name = "Queja de persona Natural"
    if request.method == "POST":
        _form_complaint = ComplaintForm(request.POST)
        _form_natural = PersonaNaturalForm(request.POST)
        if _form_complaint.is_valid() or _form_natural.is_valid():
            _complaint = Complaint(_form_complaint) #args
            _person = PersonaJuridica(_form_natural)
            _person.save()
            _complaint.is_natural = False
            _complaint.person_juridic = _person
            _complaint.enterDate = timezone.now()
            _complaint.save()
            p = WaitingForDistribution()
            p.complaint = _complaint
            p.enterDate = timezone.now()
            p.save()
            return redirect(reverse_lazy('index_natural_complaint'))
    else:
        _form_complaint = ComplaintForm()
        _form_natural = PersonaNaturalForm()
    return render(request, "dpv_complaint/multiform_complaint.html", {'form_one':_form_complaint, 'form_two': _form_natural, 'form_name': _form_name})

def form_WaitingForDistribution(request):
    _form_name = "Quejas por distribuir"
    if request.method == "POST":
        _form = WaitingForDistributionForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit=False)
            _post._enterDate=timezone.now()
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
            _post._enterDate = timezone.now()
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
            _post._enterDate = timezone.now()
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
            _post.enterDate = timezone.now()
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy())
    else:
        _form = FinishedComplaintForm()
    return render(request, "", {'form':_form, 'form_name': _form_name})

# Index

### Indexing complaint, Natural and Juridic
def index_NaturalComplaint(request):
    index_name = 'Indice de las Quejas'
    elems = Complaint.objects.filter(is_natural = True)
    return render(request, "dpv_complaint/index_natural_complaint.html", {'index': elems, 'index_name': index_name})

def index_JuridicComplaint(request):
    index_name = 'Indice de las Quejas'
    elems = Complaint.objects.filter(_is_natural = False)
    return render(request, "dpv_complaint/index_juridic_complaint.html", {'index': elems, 'index_name': index_name})

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

temp_complaint = None
# Mov from state to state
def from_waitingForDistribution_to_asignedToTecnic(request, complaint):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AsignedToTecnicForm(request.POST)
        if _form.is_valid():
            if complaint is None:
                complaint = temp_complaint
                temp_complaint = None
            _post = _form.save(commit=False)
            _post.enterDate = timezone.now()
            # todo Get information of Complaint
            _post.complaint = Complaint.objects.get(id=complaint)
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy("index_asigned_to_tecnic"))
    else:
        temp_complaint = complaint
        _form = FinishedComplaintForm()
    return render(request, "dpv_complaint/trans_wait_to_asignedToTecnic.html", {'form': _form, 'form_name': _form_name})

    pass

def from_asignedToTecnic_to_finishedComplaint(request, complaint):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AsignedToTecnicForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit=False)
            _post.enterDate = timezone.now()
            # ###todo Get information of complaint
            # comp_get = request.GET.get('complaint_num','')
            if complaint is not None:
                _post.complaint = Complaint.objects.get(id=complaint)
                _post.id = _post.pk
                _post.save()
                return redirect(reverse_lazy("index_finished_complaint"))
    else:
        _form = FinishedComplaintForm()
    return render(request, "dpv_complaint/trans_asignedToTecnic_to_finishedComp.html", {'form': _form, 'form_name': _form_name})

def from_finishedComplaint_to_acceptedComplaint(request, complaint_id, tecnic_id):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AcceptedForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit=False)
            _post.finishedDate = timezone.now()
            # todo Get information of the complaint
            # comp_get = request.GET.get('complaint_num', '')
            # boss_get = request.GET.get('boss_num', '')
            # tecnic_get = request.GET.get('tecnic_num', '')
            if (complaint_id is not None) and (tecnic_id is not None):

                _post.complaint = Complaint.objects.get(id=complaint_id)
                # todo Get information of the boss
                # _post.bossAccepted = Perfil.objects.get(id=boss_id)
                ##########
                # todo Get information of the tecnic
                _post.tecnicWorkInComplaint = Tecnic.objects.get(tecnic_id)
                _post.id = _post.pk
                _post.save()
                return redirect(reverse_lazy('index_accepted'))
    else:
        _form = AcceptedForm()
    return render(request, "dpv_complaint/trans_finished_to_ accepted.html", {'form': _form, 'form_name': _form_name})
    pass

#def from_finishedComplaint_to_reAsignedToTenic(request):
#    pass

