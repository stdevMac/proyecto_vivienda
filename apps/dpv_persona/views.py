from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required


# Create your views here.
@login_required()
def index(request):
    return render(request, 'dpv_persona/list.html')


@permission_required('personajuridica.view_personajuridica', raise_exception=True)
def index_persojur(request):
    return render(request, 'dpv_persona/list_persojur.html')


@permission_required('personanatural.view_personanatural', raise_exception=True)
def index_personat(request):
    return render(request, 'dpv_persona/list_personat.html')