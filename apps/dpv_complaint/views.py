from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import  *
from .models import *

# Create your views here.

def form_Complaint(request):
    form_name = "Queja"
    if request.method == "POST":
        form = PresentedComplaintNaturalForm(request.POST)
        if form.is_valid():
            complaint = Complaint()
            post = form.save(commit=False)
            post.enter_date = timezone.now()
            post.id = post.pk
            post.save()
            return redirect(reverse_lazy('naturalPerson'))
    else:
        form = PresentedComplaintNaturalForm()
    return render(request, "dpv_complaint/create_complaint.html", {'form': form,'form_name': form_name})
