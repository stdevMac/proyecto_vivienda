from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.decorators import permission_required, login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
@login_required()
def index(request):
    return render(request, 'dpv_nomencladores/list.html')


@permission_required('provincia.view_provincia', raise_exception=True)
def index_provincia(request):
    provincias = models.Provincia.objects.all()
    return render(request, 'dpv_nomencladores/list_provincia.html', {'provincias': provincias})


class ProvinciaCreate(CreateView):
    model = models.Provincia
    form_class = forms.ProvinciaForm
    template_name = 'dpv_nomencladores/list_provincia.html'
    success_url = reverse_lazy('nomenclador_provincia')


class ProvinciaUpdate(UpdateView):
    model = models.Provincia
    form_class = forms.ProvinciaForm
    template_name = 'dpv_nomencladores/list_provincia.html'
    success_url = reverse_lazy('nomenclador_provincia')


@permission_required('municipio.view_municipio', raise_exception=True)
def index_municipio(request):
    municipios = models.Municipio.objects.all()
    return render(request, 'dpv_nomencladores/list_municipio.html', {'municipios': municipios})


@permission_required('calle.view_calle', raise_exception=True)
def index_calle(request):
    calles = models.Calle.objects.all()
    return render(request, 'dpv_nomencladores/list_calle.html', {'calles': calles})


@permission_required('piso.view_piso', raise_exception=True)
def index_piso(request):
    pisos = models.Piso.objects.all()
    return render(request, 'dpv_nomencladores/list_piso.html', {'pisos': pisos})


@permission_required('organismo.view_organismo', raise_exception=True)
def index_organismo(request):
    organismos = models.Organismo.objects.all()
    return render(request, 'dpv_nomencladores/list_organismo.html', {'organismos': organismos})


@permission_required('destino.view_destino', raise_exception=True)
def index_destino(request):
    destinos = models.Destino.objects.all()
    return render(request, 'dpv_nomencladores/list_destino.html', {'organismos': destinos})


@permission_required('concepto.view_concepto', raise_exception=True)
def index_concepto(request):
    conceptos = models.Concepto.objects.all()
    return render(request, 'dpv_nomencladores/list_concepto.html', {'conceptos': conceptos})


@permission_required('genero.view_genero', raise_exception=True)
def index_genero(request):
    generos = models.Genero.objects.all()
    return render(request, 'dpv_nomencladores/list_genero.html', {'generos': generos})


@permission_required('areatrabajo.view_areatrabajo', raise_exception=True)
def index_areatrabajo(request):
    departamentos = models.AreaTrabajo.objects.all()
    return render(request, 'dpv_nomencladores/list_areatrabajo.html', {'departamentos': departamentos})


@permission_required('centrotrabajo.view_centrotrabajo', raise_exception=True)
def index_centrotrabajo(request):
    unidades = models.CentroTrabajo.objects.all()
    return render(request, 'dpv_nomencladores/list_centrotrabajo.html', {'unidades': unidades})