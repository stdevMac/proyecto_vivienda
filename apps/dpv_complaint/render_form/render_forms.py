from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.dpv_complaint.forms import *
from apps.dpv_complaint.models import *


@permission_required('dpv_complaint.add_accepted')
def form_accepted(request, finished_id):
    form_name = "Quejas Aceptadas"
    if request.method == "POST":
        form = AcceptedForm(request.POST)
        if form.is_valid():
            finished = FinishedComplaint.objects.get(id=finished_id)
            post = form.save(commit=False)
            post.finished_date = timezone.now()
            post.complaint = finished.complaint
            post.technical_work_in_complaint = finished.technical
            post.technical_args = finished.technical_args
            post.boss_accepted = Perfil.objects.get(id=request.user.id)
            post.id = post.pk

            history = HistoryComplaint(complaint=Complaint.objects.get(id=finished.complaint.id),
                                       current_status='Finalizada')
            history.save()
            post.save()
            return redirect(reverse_lazy('index_accepted'))
    else:
        form = AcceptedForm()
    return render(request, "", {'form': form, 'form_name': form_name})


@permission_required('dpv_complaint.change_complaint')
def assign_department(request, complaint_id):
    form_name = "Asignar Departamento"
    if request.method == 'POST':
        form = AssignDepartmentForm(request.POST)
        if form.is_valid():
            args = form.fields['department'].queryset.first()
            complaint = Complaint.objects.filter(id=complaint_id).update(department=args,
                                                                         assigned_to_department_date=timezone.now())
            history = HistoryComplaint(assigned_by=Perfil.objects.get(id=request.user.id), complaint=Complaint.objects.get(id=complaint),
                                       current_status='Esperando Asignación')
            history.save()

            return redirect(reverse_lazy('index_natural_complaint'))
    else:
        form = AssignDepartmentForm()
    return render(request, 'dpv_complaint/single_form.html', {'form': form, 'form_name': form_name})

