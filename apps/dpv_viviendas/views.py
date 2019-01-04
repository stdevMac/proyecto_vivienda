from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Vivienda
from .forms import ViviendaForm
from django.contrib.auth.decorators import permission_required, login_required


# Create your views here.
@permission_required('dpv_viviendas.view_vivienda', raise_exception=True)
def index(request):
    viviendas = Vivienda.objects.none()
    try:
        perfil = request.user.perfil_usuario
        try:
            ct = perfil.centro_trabajo
            if ct.oc:
                viviendas = Vivienda.objects.all()
            else:
                viviendas = Vivienda.objects.filter(local_dado__municipio=ct.municipio)
        except:
            print("no tiene centro de trabajo asociado")
    except:
        print("no tiene perfil asociado")
    return render(request, "dpv_viviendas/list.html", {'viviendas': viviendas})

@permission_required('dpv_viviendas.add_vivienda', raise_exception=True)
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

@permission_required('dpv_viviendas.change_vivienda', raise_exception=True)
def vivienda_edit(request, id_vivienda):
    viv = Vivienda.objects.filter(id=id_vivienda).first()
    if request.method == 'POST':
        form = ViviendaForm(request.POST, instance=viv)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('vivienda_list'))
    else:
        form = ViviendaForm(instance=viv)
    return render(request, 'dpv_viviendas/form.html', {'form': form})

