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
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AcceptedForm(request.POST)
        if _form.is_valid():
            finished = FinishedComplaint.objects.get(id=finished_id)
            _post = _form.save(commit=False)
            _post.finished_date = timezone.now()
            _post.complaint = finished.complaint
            _post.technical_work_in_complaint = finished.technical
            _post.technical_args = finished.technical_args
            _post.bossAccepted = request.user.id
            _post.id = _post.pk
            _post.save()
            return redirect(reverse_lazy('index_accepted'))
    else:
        _form = FinishedComplaintForm()
    return render(request, "", {'form': _form, 'form_name': _form_name})


def form_assign_department(request, complaint_id):
    form_name = "Asignar Departamento"
    if request.method == 'POST':
        form = AssignDepartmentForm(request.POST)
        if form.is_valid():
            args = form.fields['department'].queryset.first()
            Complaint.objects.filter(id=complaint_id).update(department=args)
            return redirect(reverse_lazy('index_natural_complaint'))
    else:
        form = AssignDepartmentForm()
    return render(request, 'dpv_complaint/single_form.html', {'form': form, 'form_name': form_name})

