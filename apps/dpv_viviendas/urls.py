from django.urls import path
from .views import index, vivienda_add, vivienda_edit

urlpatterns = [
    path('', index, name='vivienda_list'),
    path('form/', vivienda_add, name='vivienda_add'),
    path('form/<int:id_vivienda>', vivienda_edit, name='vivienda_edit'),
]