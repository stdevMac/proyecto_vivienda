from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .forms import *
from .models import *


def main_view(request):
    return render(request, "dpv_complaint/complaint_main_page.html")


def from_waiting_for_distribution_to_assigned_to_technician(request, complaint_id):
    form_name = "Seleccionar Tecnico"
    if request.method == "POST":
        form = AssignedToTechnicalForm(request.POST)
        if form.is_valid():
            # history = HistoryComplaint()
            post = form.save(commit=False)
            post.enter_date = timezone.now()
            post.complaint = Complaint.objects.get(id=complaint_id)
            Complaint.objects.filter(id=complaint_id).update(status='Esperando Respuesta de Tecnico')
            post.complaint.status = 'Esperando Respuesta de Tecnico'
            post.complaint.save()
            post.id = post.pk
            post.save()
            return redirect(reverse_lazy('index_assigned_to_technical', args=[post.technical.id]))
    else:
        form = AssignedToTechnicalForm()
    return render(request, "dpv_complaint/single_form.html", {'form': form, 'form_name': form_name})


def watch_complaint(request, complaint_id):
    complaint = Complaint.objects.filter(id=complaint_id)
    return render(request, "dpv_complaint/watch_complaint.html", {'complaint': complaint})


def from_assigned_to_technician_to_finished_complaint(request, complaint_id, technical_id):
    form_name = "Dar Respuesta a la Queja"
    if request.method == "POST":
        form = FinishedComplaintForm(request.POST)
        if form.is_valid() and complaint_id is not None and technical_id is not None:
                post = form.save(commit=False)
                post.enterDate = timezone.now()
                post.complaint = Complaint.objects.get(id=complaint_id)
                post.technical = Technical.objects.get(id=technical_id)
                Complaint.objects.filter(id=complaint_id).update(status='Esperando aceptacion del jefe')
                post.id = post.pk
                AssignedToTechnician.objects.filter(technical=post.technical).filter(complaint=post.complaint).delete()
                doc = Documents()
                doc.text = post.technical_args
                doc.save()
                post.technical_args = doc
                post.save()
                return redirect(reverse_lazy('index_assigned_to_technical', args=technical_id))
    else:
        form = FinishedComplaintForm()
    return render(request, "dpv_complaint/asigned_to_finished.html", {'form': form, 'form_name': form_name})


def index_accepted_all(request, accepted_id):
    elms = Accepted.objects.get(id=accepted_id)
    return render(request, 'dpv_complaint/watch_accepted.html', {'index': elms})


def from_finished_complaint_to_accepted_complaint(request, complaint_id, technical_id):
    form_name = "Quejas Aceptadas"
    if request.method == "POST":
        form = AcceptedForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.finishedDate = timezone.now()
            if (complaint_id is not None) and (technical_id is not None):

                post.complaint = Complaint.objects.get(id=complaint_id)
                post.technical_work_in_complaint = Technical.objects.get(id=technical_id)
                post.boss_accepted = Perfil.objects.get(id=1)
                post.id = post.pk
                # Set in history
                history = HistoryComplaint()
                # history.
                # Delete finished complaint args
                FinishedComplaint.objects.filter(complaint=complaint_id).filter(technical=technical_id).delete()
                post.save()
                return redirect(reverse_lazy('index_accepted_all'))
    else:
        form = AcceptedForm()
    return render(request, "dpv_complaint/single_form.html", {'form': form, 'form_name': form_name})
