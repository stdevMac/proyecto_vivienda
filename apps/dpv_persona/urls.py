from django.urls import path
from .views import index, index_persojur, index_personat, add_personat, add_personjur

urlpatterns = [
    path('', index, name='persona_list'),
    path('natural/', index_personat, name='persona_natural'),
    path('juridica/', index_persojur, name='persona_juridica'),
    path('natural/form/', add_personat, name='persona_natural_add'),
    path('juridica/form/', add_personjur, name='persona_juridica_add'),
]