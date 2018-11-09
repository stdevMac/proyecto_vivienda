from django.shortcuts import render
from .models import Vivienda


# Create your views here.
def index(request):
    viviendas = Vivienda.objects.all()
    return render(request, "dpv_viviendas/list.html", {'viviendas': viviendas})