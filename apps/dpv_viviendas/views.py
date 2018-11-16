from django.shortcuts import render
from .models import Vivienda
from django.contrib.auth.decorators import permission_required, login_required


# Create your views here.
@permission_required('vivienda.view_vivienda', raise_exception=True)
def index(request):
    viviendas = Vivienda.objects.all()
    return render(request, "dpv_viviendas/list.html", {'viviendas': viviendas})