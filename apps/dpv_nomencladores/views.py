from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'dpv_nomencladores/list.html')


def index_provincia(request):
    return render(request, 'dpv_nomencladores/list_provincia.html')


def index_municipio(request):
    return render(request, 'dpv_nomencladores/list_municipio.html')


def index_calle(request):
    return render(request, 'dpv_nomencladores/list_calle.html')


def index_piso(request):
    return render(request, 'dpv_nomencladores/list_piso.html')


def index_organismo(request):
    return render(request, 'dpv_nomencladores/list_organismo.html')


def index_destino(request):
    return render(request, 'dpv_nomencladores/list_destino.html')


def index_concepto(request):
    return render(request, 'dpv_nomencladores/list_concepto.html')


def index_genero(request):
    return render(request, 'dpv_nomencladores/list_genero.html')


def index_areatrabajo(request):
    return render(request, 'dpv_nomencladores/list_areatrabajo.html')


def index_centrotrabajo(request):
    return render(request, 'dpv_nomencladores/list_centrotrabajo.html')