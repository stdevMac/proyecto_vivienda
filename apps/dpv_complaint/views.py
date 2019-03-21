from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .forms import *
from .models import *


def main_view(request):
    return render(request, "dpv_complaint/complaint_main_page.html")


def from_waiting_for_distribution_to_assigned_to_technician(request, complaint_id):
    form_name = "Seleccione técnico"
    if request.method == "POST":
        form = AssignedToTechnicalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.enter_date = timezone.now()
            post.assigned_by = Perfil.objects.get(id=request.user.id)
            post.complaint = Complaint.objects.get(id=complaint_id)
            Complaint.objects.filter(id=complaint_id).update(status='Esperando respuesta de técnico')
            post.complaint.status = 'Esperando respuesta de técnico'
            post.complaint.save()
            post.id = post.pk
            post.save()

            # Set in history
            history = HistoryComplaint()
            history.complaint = post.complaint
            history.date_of_status = WaitingForDistribution.objects.filter(id=post.complaint.id).\
                first().enter_date
            history.current_status = 'Esperando Asignación'
            history.save()

            WaitingForDistribution.objects.filter(id=post.complaint.id).delete()

            return redirect(reverse_lazy('index_assigned_to_technical', args=[post.technical.id]))
    else:
        form = AssignedToTechnicalForm()
    return render(request, "dpv_complaint/single_form.html", {'form': form, 'form_name': form_name})


def from_assigned_to_technician_to_finished_complaint(request, complaint_id, technical_id):
    form_name = "Dar respuesta a la queja"
    if request.method == "POST":
        form = FinishedComplaintForm(request.POST)
        if form.is_valid() and complaint_id is not None and technical_id is not None:
                post = form.save(commit=False)
                post.enter_date = timezone.now()
                post.complaint = Complaint.objects.get(id=complaint_id)
                post.technical = Technical.objects.get(id=technical_id)
                Complaint.objects.filter(id=complaint_id).update(status='Esperando aceptación del jefe')
                post.id = post.pk
                enter_date = AssignedToTechnician.objects.filter(technical=post.technical).\
                    filter(complaint=post.complaint).first().enter_date
                AssignedToTechnician.objects.filter(technical=post.technical).filter(complaint=post.complaint).delete()
                post.save()

                # Set in history
                history = HistoryComplaint()
                history.complaint = post.complaint
                history.technical = post.technical
                history.technical_args = post.technical_args
                history.date_of_status = enter_date
                history.current_status = 'Esperando Respuesta de Técnico'
                history.save()

                return redirect(reverse_lazy('index_assigned_to_technical', args=technical_id))
    else:
        form = FinishedComplaintForm()
    return render(request, "dpv_complaint/assigned_to_finished.html", {'form': form, 'form_name': form_name})


def from_finished_complaint_to_accepted_complaint(request, complaint_id, technical_id):
    form_name = "Quejas aceptadas"
    if request.method == "POST":
        form = AcceptedForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.finishedDate = timezone.now()
            if (complaint_id is not None) and (technical_id is not None):

                Complaint.objects.filter(id=complaint_id).update(status='Finalizada')
                post.complaint = Complaint.objects.get(id=complaint_id)
                post.technical_work_in_complaint = Technical.objects.get(id=technical_id)
                post.boss_accepted = Perfil.objects.get(id=request.user.id)
                post.id = post.pk
                post.technical_args = FinishedComplaint.objects.filter(complaint=complaint_id).\
                    filter(technical=technical_id).first().technical_args
                enter_date = FinishedComplaint.objects.filter(complaint=complaint_id).filter(technical=technical_id)
                FinishedComplaint.objects.filter(complaint=complaint_id).filter(technical=technical_id).delete()

                # Set in history
                history = HistoryComplaint()
                history.complaint = post.complaint
                history.technical = post.technical_work_in_complaint
                history.technical_args = post.technical_args
                history.date_of_status = enter_date
                history.current_status = 'Esperando aceptación del jefe'
                history.save()

                # Delete finished complaint args
                post.save()
                return redirect(reverse_lazy('index_accepted_all'))
    else:
        form = AcceptedForm()
    return render(request, "dpv_complaint/single_form.html", {'form': form, 'form_name': form_name})
