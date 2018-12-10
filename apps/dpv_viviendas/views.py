from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Vivienda
from .forms import ViviendaForm
from django.contrib.auth.decorators import permission_required, login_required


# Create your views here.
@permission_required('vivienda.view_vivienda', raise_exception=True)
def index(request):
    viviendas = Vivienda.objects.all()
    return render(request, "dpv_viviendas/list.html", {'viviendas': viviendas})


def vivienda_add(request):
    if request.method == 'POST':
        form = ViviendaForm(request.POST)
        if form.is_valid():
            form.save()
            redirect(reverse_lazy('vivienda_list'))
        else:
            return render(request, 'dpv_viviendas/form.html', {'form': form})
    else:
        form = ViviendaForm()
        return render(request, 'dpv_viviendas/form.html', {'form': form})
