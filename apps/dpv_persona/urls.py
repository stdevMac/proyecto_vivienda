from django.urls import path
from .views import index, index_persojur, index_personat

urlpatterns = [
    path('', index, name='persona_list'),
    path('natural/', index_personat, name='persona_natural'),
    path('jurdica/', index_persojur, name='persona_juridica'),
]