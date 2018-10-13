from django.shortcuts import render


def view_main(request):
    return render(request, 'layouts/base.html')
