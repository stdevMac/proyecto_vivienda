### Indexing complaint, Natural and Juridic
from django.shortcuts import render
from apps.dpv_complaint.models import *


def index_NaturalComplaint(request):
    index_name = 'Indice de las Quejas'
    elems = Complaint.objects.filter(is_natural = True)
    return render(request, "dpv_complaint/index_complaint.html", {'index': elems, 'index_name': index_name})


def index_JuridicComplaint(request):
    index_name = 'Indice de las Quejas'
    elems = Complaint.objects.filter(_is_natural = False)
    return render(request, "dpv_complaint/index_complaint.html", {'index': elems, 'index_name': index_name})


def index_WaitingForDistribution(request):
    index_name = 'Indice de Quejas en espera de su distribucion'
    elems = Complaint.objects.filter(department=None)
    return render(request, "dpv_complaint/index_waiting_for_distribution.html", {'index': elems, 'index_name' : index_name })


def index_AsignedToTecnic(request, tecnic_id):
    comp = AsignedToTecnic.objects.filter(tecnic=tecnic_id)
    index_name = 'Quejas asignadas al Tecnico Fulano de tal'
    elems = [x.complaint for x in comp ]
    return render(request, "dpv_complaint/index_complaint.html", {'index': elems, 'index_name' : index_name })



def index_FinishedComplaint(request):
    index_name = 'Indice de Quejas Finalizadas'
    elems = FinishedComplaint.objects.all()
    return render(request, "dpv_complaint/index_finished.html", { 'index': elems, 'index_name': index_name})


def index_Accepted(request):
    index_name = 'Indice de Quejas Aceptadas'
    elems = Accepted.objects.all()
    return render(request, "dpv_complaint/index_accepted.html", {'index': elems, 'index_name': index_name})

