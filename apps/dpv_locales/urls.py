from django.urls import path
from .views import index, stats, local_add

urlpatterns = [
    path('', index, name='locales_list'),
    path('estadistico/', stats, name='locales_stats'),
    path('form/', local_add, name='locales_add'),
]