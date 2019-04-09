from django.shortcuts import render
from apps.dpv_complaint.models import *


def index_natural_complaint(request):
    index_name = 'Índice de las Quejas'
    elms = Complaint.objects.filter(is_natural=True)
    return render(request, "dpv_complaint/index_complaint_new.html", {'index': elms, 'index_name': index_name})


def index_juridic_complaint(request):
    index_name = 'Índice de las Quejas'
    elms = Complaint.objects.filter(is_natural=False)
    return render(request, "dpv_complaint/index_complaint_new.html", {'index': elms, 'index_name': index_name})


def index_waiting_for_distribution(request):
    index_name = 'Índice de Quejas en espera de su distribución'
    elms = Complaint.objects.filter(department=None)
    return render(request, "dpv_complaint/index_waiting_for_distribution.html",
                  {'index': elms, 'index_name': index_name})


def index_assigned_to_technician(request, technical_id):
    technical = Technical.objects.get(id=technical_id)
    comp = AssignedToTechnician.objects.filter(technical=technical_id)
    index_name = 'Quejas asignadas al técnico' + technical.profile.datos_personales.nombre + ' ' + \
                 technical.profile.datos_personales.apellidos
    return render(request, "dpv_complaint/index_assigned_to_technical.html",
                  {'index': comp, 'index_name': index_name, 'technical_id': technical_id,
                   'technical_name': technical.profile.datos_personales.nombre + ' ' +
                                     technical.profile.datos_personales.apellidos})


def index_technical(request):
    index_name = 'Índice técnicos'
    technical = Technical.objects.all()
    return render(request, 'dpv_complaint/index_technical.html', {'index': technical, 'index_name': index_name})


def index_finished_complaint(request):
    index_name = 'Índice de Quejas Finalizadas'
    elms = FinishedComplaint.objects.all()
    return render(request, "dpv_complaint/index_finished.html", {'index': elms, 'index_name': index_name})


def index_accepted(request):
    index_name = 'Índice de Quejas Aceptadas'
    elms = Accepted.objects.all()
    return render(request, "dpv_complaint/index_accepted_new.html", {'index': elms, 'index_name': index_name})


def watch_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    person = None
    if not complaint.anonymous:
        if complaint.is_natural:
            person = PersonaNatural.objects.get(id=complaint.person_natural.id)
            pass
        else:
            person = PersonaJuridica.objects.get(id=complaint.person_juridic.id)
    else:
        # TODO Anonymous
        pass
    return render(request, "dpv_complaint/watch_complaint.html", {'complaint_for_dist': complaint, 'person': person})


def watch_finished(request, finished_id):
    complaint = FinishedComplaint.objects.filter(id=finished_id)
    return render(request, "dpv_complaint/watch_finished.html", {'index': complaint,
                                                                 'index_name': 'Datos queja finalizada'})


def index_accepted_all(request, accepted_id):
    elms = Accepted.objects.filter(id=accepted_id)
    return render(request, 'dpv_complaint/watch_accepted.html', {'index': elms})
