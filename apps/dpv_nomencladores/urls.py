from django.urls import path
from .views import index, index_calle, index_concepto, index_destino, index_genero, index_municipio, index_organismo, \
                   index_piso, index_provincia, index_areatrabajo, index_centrotrabajo

urlpatterns = [
    path('', index, name='nomenclador_index'),
    path('provincia/', index_provincia, name='nomenclador_provincia'),
    path('municipio/', index_municipio, name='nomenclador_municipio'),
    path('calle/', index_calle, name='nomenclador_calle'),
    path('piso/', index_piso, name='nomenclador_piso'),
    path('genero/', index_genero, name='nomenclador_genero'),
    path('concepto/', index_concepto, name='nomenclador_concepto'),
    path('destino/', index_destino, name='nomenclador_destino'),
    path('organismo/', index_organismo, name='nomenclador_organismo'),
    path('areatrabajo/', index_areatrabajo, name='nomenclador_areatrab'),
    path('centrotrabajo/', index_centrotrabajo, name='nomenclador_centrab'),
]