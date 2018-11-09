from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    return render(request, 'dpv_nomencladores/list.html')


def index_provincia(request):
    provincias = models.Provincia.objects.all()
    return render(request, 'dpv_nomencladores/list_provincia.html', {'provincias': provincias})


def index_municipio(request):
    municipios = models.Municipio.objects.all()
    return render(request, 'dpv_nomencladores/list_municipio.html', {'municipios': municipios})


def index_calle(request):
    calles = models.Calle.objects.all()
    return render(request, 'dpv_nomencladores/list_calle.html', {'calles': calles})


def index_piso(request):
    pisos = models.Piso.objects.all()
    return render(request, 'dpv_nomencladores/list_piso.html', {'pisos': pisos})


def index_organismo(request):
    organismos = models.Organismo.objects.all()
    return render(request, 'dpv_nomencladores/list_organismo.html', {'organismos': organismos})


def index_destino(request):
    destinos = models.Destino.objects.all()
    return render(request, 'dpv_nomencladores/list_destino.html', {'organismos': destinos})


def index_concepto(request):
    conceptos = models.Concepto.objects.all()
    return render(request, 'dpv_nomencladores/list_concepto.html', {'conceptos': conceptos})


def index_genero(request):
    generos = models.Genero.objects.all()
    return render(request, 'dpv_nomencladores/list_genero.html', {'generos': generos})


def index_areatrabajo(request):
    departamentos = models.AreaTrabajo.objects.all()
    return render(request, 'dpv_nomencladores/list_areatrabajo.html', {'departamentos': departamentos})


def index_centrotrabajo(request):
    unidades = models.CentroTrabajo.objects.all()
    return render(request, 'dpv_nomencladores/list_centrotrabajo.html', {'unidades': unidades})