from django.shortcuts import render
from apps.dpv_complaint.models import *


def index_natural_complaint(request):
    index_name = 'Indice de las Quejas'
    elms = Complaint.objects.filter(is_natural = True)
    return render(request, "dpv_complaint/index_complaint_new.html", {'index': elms, 'index_name': index_name})


def index_juridic_complaint(request):
    index_name = 'Indice de las Quejas'
    elms = Complaint.objects.filter(is_natural = False)
    return render(request, "dpv_complaint/index_complaint_new.html", {'index': elms, 'index_name': index_name})


def index_waiting_for_distribution(request):
    index_name = 'Indice de Quejas en espera de su distribucion'
    elms = Complaint.objects.filter(department=None)
    return render(request, "dpv_complaint/index_waiting_for_distribution.html", {'index': elms, 'index_name' : index_name })


def index_assigned_to_technician(request, tecnic_id):
    comp = AssignedToTechnician.objects.filter(tecnic=tecnic_id)
    index_name = 'Quejas asignadas al Tecnico Fulano de tal'
    elms = [x.complaint for x in comp]
    return render(request, "dpv_complaint/index_asigned_to_tecnic.html", {'index': elms, 'index_name' : index_name , 'tecnic_id':tecnic_id})


def index_finished_complaint(request):
    index_name = 'Indice de Quejas Finalizadas'
    elms = FinishedComplaint.objects.all()
    return render(request, "dpv_complaint/index_finished.html", { 'index': elms, 'index_name': index_name})


def index_accepted(request):
    index_name = 'Indice de Quejas Aceptadas'
    elms = Accepted.objects.all()
    return render(request, "dpv_complaint/index_accepted.html", {'index': elms, 'index_name': index_name})

