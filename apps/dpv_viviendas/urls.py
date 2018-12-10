from django.urls import path
from .views import index, vivienda_add

urlpatterns = [
    path('', index, name='vivienda_list'),
    path('form/', vivienda_add, name='vivienda_add'),
]