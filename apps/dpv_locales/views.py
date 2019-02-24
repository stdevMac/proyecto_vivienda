from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import F, Q, Sum, Count
from django.db.models.query import QuerySet
from django.views.generic import View
from django.contrib.auth.decorators import permission_required
from .models import Local
from .forms import LocalForm
from apps.dpv_nomencladores.models import Municipio


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
        if not request.user.perfil_usuario.centro_trabajo.oc:
            local = Local()
            local.municipio = request.user.perfil_usuario.centro_trabajo.municipio
            form = LocalForm(instance=local)
        else:
            form = LocalForm()
        return render(request, 'dpv_locales/form.html', {'form': form})


# @permission_required('dpv_locales.view_local', raise_exception=True)
def stats(request, id_municipio=None):
    result = []

    if not id_municipio and request.user.perfil_usuario.centro_trabajo.oc:
        if Local.objects.all().count() > 0:
            for m in Municipio.objects.all():
                q = Local.objects.filter(municipio=m).aggregate(cant_viv=Sum('no_viviendas'), cant_pend_viv=Sum('pendiente'), cant_loc=Count('fecha'), statales=Sum('estatal'))
                qm = {"nombre": m.nombre, "id": m.id, "tipo": 'municpio'}
                qr = dict(qm, **q)
                result.append(qr)
    elif not id_municipio and not request.user.perfil_usuario.centro_trabajo.oc:
        if Local.objects.all().count() > 0:
            for cp in request.user.perfil_usuario.centro_trabajo.municipio.consejos.all():
                q = Local.objects.filter(consejo_popular=cp).aggregate(cant_viv=Sum('no_viviendas'), cant_pend_viv=Sum('pendiente'), cant_loc=Count('fecha'), statales=Sum('estatal'))
                qm = {"nombre": cp.nombre, "id": cp.id, "tipo": 'consejo'}
                qr = dict(q, **qm)
                result.append(qr)
    else:
        if Local.objects.filter(id=id_municipio).count() > 0:
            for cp in Municipio.objects.filter(id=id_municipio).first().consejos.all():
                q = Local.objects.filter(consejo_popular=cp).aggregate(cant_viv=Sum('no_viviendas'), cant_pend_viv=Sum('pendiente'), cant_loc=Count('fecha'), statales=Sum('estatal'))
                qm = {"nombre": cp.nombre, "id": cp.id, "tipo": 'consejo'}
                qr = dict(q, **qm)
                result.append(qr)

    return render(request, 'dpv_locales/estdistico.html', {'result': result})


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

