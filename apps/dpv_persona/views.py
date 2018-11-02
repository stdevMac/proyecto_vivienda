from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dpv_persona/list.html')