from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import F, Q, Sum, Count
from django.views.generic import View
from .models import Local
from .forms import LocalForm
from django.contrib.auth.decorators import permission_required


# Create your views here.
@permission_required('dpv_locales.view_local', raise_exception=True)
def index(request):
    locales = Local.objects.none()
    try:
        perfil = request.user.perfil_usuario
        try:
            ct = perfil.centro_trabajo
            if ct.oc:
                locales = Local.objects.all()
            else:
                locales = Local.objects.filter(municipio=ct.municipio)
        except:
            print("no tiene centro de trabajo asociado")
    except:
        print("no tiene perfil asociado")
    return render(request, 'dpv_locales/list.html', {'locales': locales})


@permission_required('dpv_locales.add_local', raise_exception=True)
def local_add(request):
    if request.method == "POST":
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dpv_locales/form.html', {'form': form})
        else:
            return render(request, 'dpv_locales/form.html', {'form': form})
    else:
        form = LocalForm()
        return render(request, 'dpv_locales/form.html', {'form': form})


@permission_required('dpv_locales.view_local', raise_exception=True)
def stats(request):
    # if request.user.perfil_usuario:
    #     perfil = request.user.perfil_usuario
    #     if perfil.centro_trabajo:
    #         if perfil.centro_trabajo.oc:
    #             locales = Local.objects.all()
    #         else:
    #             locales = Local.objects.filter(municipio=perfil.centro_trabajo.municipio)
    #     else:
    #         locales = Local.objects.none()
    # else:
    #     locales = Local.objects.none()
    locales = Local.objects.all()
    return render(request, 'dpv_locales/estdistico.html', {'locales': locales})


def local_edit(request, id_local):
    lol = Local.objects.filter(id=id_local).first()
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=lol)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('locales_list'))
    else:
        form = LocalForm(instance=lol)
    return render(request, 'dpv_locales/form.html', {'form': form})

