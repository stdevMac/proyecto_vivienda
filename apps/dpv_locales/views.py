from django.shortcuts import render
from django.db.models import F, Q, Sum, Count
from django.views.generic import View
from .models import Local
from django.contrib.auth.decorators import permission_required


# Create your views here.
@permission_required('local.view_local', raise_exception=True)
def index(request):
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
    return render(request, 'dpv_locales/list.html', {'locales': locales})

