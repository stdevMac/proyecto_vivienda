from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'dpv_persona/list.html')


def index_persojur(request):
    return render(request, 'dpv_persona/list_persojur.html')


def index_personat(request):
    return render(request, 'dpv_persona/list_personat.html')