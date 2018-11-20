from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .forms import *
from .models import *

from apps.dpv_persona.forms import *

# Create Forms

def from_waitingForDistribution_to_asignedToTecnic(request, complaint):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AsignedToTecnicForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit=False)
            _post.enterDate = timezone.now()
            _post.complaint = Complaint.objects.get(id=complaint)
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy("index_asigned_to_tecnic"))
    else:
        _form = FinishedComplaintForm()
    return render(request, "dpv_complaint/single_form.html", {'form': _form, 'form_name': _form_name})



def watch_complaint(request, complaint_id):
    complaint = Complaint.objects.filter(id=complaint_id)
    return render(request, "dpv_complaint/watch_complaint.html", { 'complaint': complaint })



def from_asignedToTecnic_to_finishedComplaint(request, complaint):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AsignedToTecnicForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit=False)
            _post.enterDate = timezone.now()
            if complaint is not None:
                _post.complaint = Complaint.objects.get(id=complaint)
                _post.id = _post.pk
                _post.save()
                return redirect(reverse_lazy("index_finished_complaint"))
    else:
        _form = FinishedComplaintForm()
    return render(request, "dpv_complaint/single_form.html", {'form': _form, 'form_name': _form_name})


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
    return render(request, "dpv_complaint/single_form.html", {'form': _form, 'form_name': _form_name})
    pass


