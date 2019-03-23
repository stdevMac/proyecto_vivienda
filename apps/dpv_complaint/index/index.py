from django.shortcuts import render
from apps.dpv_complaint.models import *


def index_natural_complaint(request):
    index_name = 'Indice de las Quejas'
    elms = Complaint.objects.filter(is_natural=True)
    return render(request, "dpv_complaint/index_complaint_new.html", {'index': elms, 'index_name': index_name})


def index_juridic_complaint(request):
    index_name = 'Indice de las Quejas'
    elms = Complaint.objects.filter(is_natural=False)
    return render(request, "dpv_complaint/index_complaint_new.html", {'index': elms, 'index_name': index_name})


def index_waiting_for_distribution(request):
    index_name = 'Indice de Quejas en espera de su distribucion'
    elms = Complaint.objects.filter(department=None)
    return render(request, "dpv_complaint/index_waiting_for_distribution.html", {'index': elms, 'index_name' : index_name })


def index_assigned_to_technician(request, technical_id):
    comp = AssignedToTechnician.objects.filter(technical=technical_id)
    index_name = 'Quejas asignadas al Tecnico Fulano de tal'
    return render(request, "dpv_complaint/index_assigned_to_technical.html",
                  {'index': comp, 'index_name': index_name, 'technical_id': technical_id})


def index_finished_complaint(request):
    index_name = 'Indice de Quejas Finalizadas'
    elms = FinishedComplaint.objects.all()
    return render(request, "dpv_complaint/index_finished.html", {'index': elms, 'index_name': index_name})


def index_accepted(request):
    index_name = 'Indice de Quejas Aceptadas'
    elms = Accepted.objects.all()
    return render(request, "dpv_complaint/index_accepted.html", {'index': elms, 'index_name': index_name})


def watch_complaint(request, complaint_id):
    complaint = Complaint.objects.filter(id=complaint_id)
    return render(request, "dpv_complaint/watch_complaint.html", {'complaint': complaint})


def watch_finished(request, finished_id):
    complaint = FinishedComplaint.objects.filter(id=finished_id)
    return render(request, "dpv_complaint/watch_finished.html", {'index': complaint,
                                                                 'index_name': 'Datos queja finalizada'})


def index_accepted_all(request, accepted_id):
    elms = Accepted.objects.filter(id=accepted_id)
    return render(request, 'dpv_complaint/watch_accepted.html', {'index': elms})
