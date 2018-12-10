from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required, login_required
from .forms import PersonaJuridicaForm, PersonaNaturalForm


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


def add_personjur(request):
    if request.method == 'POST':
        form = PersonaJuridicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('persona_juridica'))
        else:
            return render(request, 'dpv_persona/form_persojur.html', {'form': form})
    else:
        form = PersonaJuridicaForm()
        return render(request, 'dpv_persona/form_persojur.html', {'form': form})


def add_personat(request):
    if request.method == 'POST':
        form = PersonaNaturalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('persona_natural'))
        else:
            return render(request, 'dpv_persona/form_personat.html', {'form': form})
    else:
        form = PersonaNaturalForm()
        return render(request, 'dpv_persona/form_personat.html', {'form': form})

