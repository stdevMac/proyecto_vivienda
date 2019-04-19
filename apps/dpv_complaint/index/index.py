from datetime import timedelta
import datetime
from django.db.models.functions import ExtractMonth
from django.contrib.auth.decorators import permission_required
from django.db.models import Count, Func, Q
from django.shortcuts import render
from apps.dpv_complaint.models import *
from apps.dpv_complaint.forms import FilterForm
from django.template.context_processors import csrf


@permission_required('dpv_complaint.view_complaint')
def index_natural_complaint(request):
    index_name = 'Índice de las Quejas'
    elms = Complaint.objects.filter(is_natural=True)
    return render(request, "dpv_complaint/index_complaint_new.html",
                  {'index': elms, 'index_name': index_name, 'natural': True})


def get_elements(cleaned_data):
    if cleaned_data['natural'] is not None:
        if cleaned_data['natural']:
            elements = Complaint.objects.filter(is_natural=True)
        else:
            elements = Complaint.objects.filter(is_natural=False)
    else:
        elements = Complaint.objects.all()

    if cleaned_data['initial_time']:
        dat = cleaned_data['final_time']
        elements = elements.filter(Q(enter_date__gte=datetime.date(dat.year, dat.month, dat.day - timedelta(1))))
    if cleaned_data['final_time']:
        dat = cleaned_data['final_time']
        elements = elements.filter(enter_date__lte=datetime.date(dat.year, dat.month, dat.day + timedelta(1)))
    if cleaned_data['municipality']:
        if cleaned_data['natural'] is not None:
            if cleaned_data['natural']:
                elements = elements.filter(person_natural__municipio=cleaned_data['municipality'])
            else:
                elements = elements.filter(person_juridic__municipio=cleaned_data['municipality'])
        else:
            elements = elements.filter(Q(person_juridic__municipio=cleaned_data['municipality']) |
                                       Q(person_natural__municipio=cleaned_data['municipality']))
    if cleaned_data['days']:
        date = min(timezone.now(), cleaned_data['final_time']) - timedelta(cleaned_data['days'])
        elements = elements.filter(enter_date__gte=date)
    if cleaned_data['status'] and cleaned_data['status'] != 'Seleccione Estado':
        elements = elements.filter(status=cleaned_data['status'])
    return elements


class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()


class MonthSqlite(Func):
    function = 'STRFTIME'
    template = '%(function)s("%%m", %(expressions)s)'
    output_field = models.CharField()


@permission_required('dpv_complaint.view_complaint')
def statistics(request):
    count_natural = Complaint.objects.filter(is_natural=True).count()
    count_juridic = Complaint.objects.filter(is_natural=False).count()
    group_month = Complaint.objects.annotate(month=ExtractMonth('enter_date')).values('month'). \
        annotate(count=Count('id')).values('month', 'count')
    return render(request, "dpv_complaint/statistics_view.html", {'dataset': group_month, 'count_nat': count_natural,
                                                                  'count_jur': count_juridic})


@permission_required('dpv_complaint.view_complaint')
def search(request):
    context = {}
    context.update(csrf(request))
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            elms = get_elements(form.cleaned_data)
            return render(request, "dpv_complaint/index_complaint_new.html",
                          {'index': elms, 'index_name': 'Elementos filtrados',
                           'natural': True if form.cleaned_data['natural'] else False})
    else:
        form = FilterForm()
    return render(request, "dpv_complaint/search_form.html", {'form': form, 'form_name': 'Plantilla de Búsqueda'})


@permission_required('dpv_complaint.view_complaint')
def index_juridic_complaint(request):
    index_name = 'Índice de las Quejas'
    elms = Complaint.objects.filter(is_natural=False)
    return render(request, "dpv_complaint/index_complaint_new.html", {'index': elms, 'index_name': index_name})


@permission_required('dpv_complaint.view_complaint')
def index_waiting_for_distribution(request):
    index_name = 'Índice de Quejas en espera de su distribución'
    elms = Complaint.objects.filter(department=None)
    return render(request, "dpv_complaint/index_waiting_for_distribution.html",
                  {'index': elms, 'index_name': index_name})


@permission_required('dpv_complaint.view_complaint')
def index_assigned_to_technician(request, technical_id):
    technical = Technical.objects.get(id=technical_id)
    comp = AssignedToTechnician.objects.filter(technical=technical_id)
    index_name = 'Quejas asignadas al técnico' + technical.profile.datos_personales.nombre + ' ' + \
                 technical.profile.datos_personales.apellidos
    return render(request, "dpv_complaint/index_assigned_to_technical.html",
                  {'index': comp, 'index_name': index_name, 'technical_id': technical_id,
                   'technical_name': technical.profile.datos_personales.nombre + ' ' +
                                     technical.profile.datos_personales.apellidos})


@permission_required('dpv_complaint.view_complaint')
def index_technical(request):
    index_name = 'Índice técnicos'
    technical = Technical.objects.all()
    return render(request, 'dpv_complaint/index_technical.html', {'index': technical, 'index_name': index_name})


@permission_required('dpv_complaint.view_complaint')
def index_finished_complaint(request):
    index_name = 'Índice de Quejas Finalizadas'
    elms = FinishedComplaint.objects.all()
    return render(request, "dpv_complaint/index_finished.html", {'index': elms, 'index_name': index_name})


@permission_required('dpv_complaint.view_complaint')
def index_accepted(request):
    index_name = 'Índice de Quejas Aceptadas'
    elms = Accepted.objects.all()
    return render(request, "dpv_complaint/index_accepted_new.html", {'index': elms, 'index_name': index_name})


@permission_required('dpv_complaint.view_complaint')
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
    technical = AssignedToTechnician.objects.filter(complaint=complaint_id)
    return render(request, "dpv_complaint/watch_complaint.html", {'complaint_for_dist': complaint,
                                                                  'person': person,
                                                                  'tech': technical.first()})


@permission_required('dpv_complaint.view_complaint')
def watch_finished(request, finished_id):
    complaint = FinishedComplaint.objects.filter(id=finished_id)
    return render(request, "dpv_complaint/watch_finished.html", {'index': complaint,
                                                                 'index_name': 'Datos queja finalizada'})


@permission_required('dpv_complaint.view_complaint')
def index_accepted_all(request, accepted_id):
    elms = Accepted.objects.filter(id=accepted_id)
    return render(request, 'dpv_complaint/watch_accepted.html', {'index': elms})
