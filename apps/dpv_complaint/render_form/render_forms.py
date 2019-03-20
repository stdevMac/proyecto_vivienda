from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.dpv_complaint.forms import *
from apps.dpv_complaint.models import *


def form_finished_complaint(request):
    _form_name = "Queja por Responder"
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
    return render(request, "dpv_complaint/single_form.html", {'form': _form, 'form_name': _form_name})


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
            post.bossAccepted = Perfil.objects.get(id=request.user.id)
            post.id = post.pk
            post.save()
            return redirect(reverse_lazy('index_accepted'))
    else:
        form = FinishedComplaintForm()
    return render(request, "", {'form': form, 'form_name': form_name})


def form_assign_department(request, complaint_id):
    form_name = "Asignar Departamento"
    if request.method == 'POST':
        form = AssignDepartmentForm(request.POST)
        if form.is_valid():
            args = form.fields['department'].queryset.first()
            complaint = Complaint.objects.filter(id=complaint_id).update(department=args,
                                                                         assigned_to_department_date=timezone.now())
            history = HistoryComplaint()
            history.complaint = complaint
            history.
            history.current_status = 'Esperando Asignación'

            history.save()
            return redirect(reverse_lazy('index_natural_complaint'))
    else:
        form = AssignDepartmentForm()
    return render(request, 'dpv_complaint/single_form.html', {'form': form, 'form_name': form_name})

