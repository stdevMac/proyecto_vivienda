from django.urls import path
from .views import index, index_persojur, index_personat, add_personat, add_personjur, edit_persojur, edit_personat

urlpatterns = [
    path('', index, name='persona_list'),
    path('natural/', index_personat, name='persona_natural'),
    path('juridica/', index_persojur, name='persona_juridica'),
    path('natural/form/', add_personat, name='persona_natural_add'),
    path('juridica/form/', add_personjur, name='persona_juridica_add'),
    path('natural/form/<int:id_personat>', edit_personat, name='persona_natural_edit'),
    path('juridica/form/<int:id_persojur>', edit_persojur, name='persona_juridica_edit'),
]