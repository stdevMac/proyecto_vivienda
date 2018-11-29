from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .forms import *
from .models import *


def main_view(request):
    return render(request, "dpv_complaint/complaint_main_page.html")


def from_waitingForDistribution_to_asignedToTecnic(request, complaint_id):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AsignedToTecnicForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit=False)
            _post.enterDate = timezone.now()
            _post.complaint = Complaint.objects.get(id=complaint_id)
            _post.complaint.status = 'Esperando Respuesta de Tecnico'
            _post.complaint.save()
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy("index_asigned_to_tecnic", tecnic_id=_post.tecnic.id))
    else:
        _form = AsignedToTecnicForm()
    return render(request, "dpv_complaint/single_form.html", {'form': _form, 'form_name': _form_name})



def watch_complaint(request, complaint_id):
    complaint = Complaint.objects.filter(id=complaint_id)
    return render(request, "dpv_complaint/watch_complaint.html", { 'complaint': complaint })



def from_asignedToTecnic_to_finishedComplaint(request, complaint_id, tecnic_id):
    _form_name = "Dar Respuesta a la Queja"
    if request.method == "POST":
        _form = FinishedComplaintForm(request.POST)
        if _form.is_valid() and complaint_id is not None and tecnic_id is not None:
                _post = _form.save(commit=False)
                _post.enterDate = timezone.now()
                _post.complaint = Complaint.objects.get(id=complaint_id)
                _post.tecnic = Tecnic.objects.get(id=tecnic_id)
                _post.id = _post.pk
                _post.save()
                return redirect(reverse_lazy( 'index_asigned_to_tecnic' ))
    else:
        _form = FinishedComplaintForm()
    return render(request, "dpv_complaint/asigned_to_finished.html", {'form': _form, 'form_name': _form_name})


def index_accepted_all(request, accepted_id):
    elems = Accepted.objects.get(id=accepted_id)
    return render(request, 'dpv_complaint/watch_accepted.html', {'index': elems})


def from_finishedComplaint_to_acceptedComplaint(request, complaint_id, tecnic_id):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AcceptedForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit=False)
            _post.finishedDate = timezone.now()
            if (complaint_id is not None) and (tecnic_id is not None):

                _post.complaint = Complaint.objects.get(id=complaint_id)
                _post.tecnicWorkInComplaint = Tecnic.objects.get(id=tecnic_id)
                _post.bossAccepted = Perfil.objects.get(id=1)
                _post.id = _post.pk
                _post.save()
                return redirect(reverse_lazy('index_accepted_all'))
    else:
        _form = AcceptedForm()
    return render(request, "dpv_complaint/single_form.html", {'form': _form, 'form_name': _form_name })