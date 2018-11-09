from django.shortcuts import render
from django.db.models import F, Q, Sum, Count
from django.views.generic import View
from .models import Local


# Create your views here.
def index(request):

    return render(request, 'dpv_locales/list.html')

