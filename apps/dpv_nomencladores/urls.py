from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='nomenclador_index'),

    path('provincia/', index_provincia, name='nomenclador_provincia'),
    path('crear_provincia/', create_provincia, name='provincia_new'),
    path('editar_provincia/', update_provincia, name='provincia_edit'),
    path('eliminar_provincia/', delete_provincia, name='provincia_delete'),

    path('municipio/', index_municipio, name='nomenclador_municipio'),
    path('crear_municipio/', create_municipio, name='municipio_new'),
    path('editar_municipio/', update_municipio, name='municipio_edit'),
    path('eliminar_municipio/', delete_municipio, name='municipio_delete'),

    path('calle/', index_calle, name='nomenclador_calle'),
    path('crear_calle/', create_calle, name='calle_new'),
    path('editar_calle/', update_calle, name='calle_edit'),
    path('eliminar_calle/', delete_calle, name='calle_delete'),

    path('piso/', index_piso, name='nomenclador_piso'),
    path('crear_piso/', create_piso, name='piso_new'),
    path('editar_piso/', update_piso, name='piso_edit'),
    path('eliminar_piso/', delete_piso, name='piso_delete'),

    path('genero/', index_genero, name='nomenclador_genero'),
    path('crear_genero/', create_genero, name='genero_new'),
    path('editar_genero/', update_genero, name='genero_edit'),
    path('eliminar_genero/', delete_genero, name='genero_delete'),

    path('concepto/', index_concepto, name='nomenclador_concepto'),
    path('crear_concepto/', create_concepto, name='concepto_new'),
    path('editar_concepto/', update_concepto, name='concepto_edit'),
    path('eliminar_concepto/', delete_concepto, name='concepto_delete'),

    path('destino/', index_destino, name='nomenclador_destino'),
    path('crear_destino/', create_destino, name='destino_new'),
    path('editar_destino/', update_destino, name='destino_edit'),
    path('eliminar_destino/', delete_destino, name='destino_delete'),

    path('organismo/', index_organismo, name='nomenclador_organismo'),
    path('crear_organismo/', create_organismo, name='organismo_new'),
    path('editar_organismo/', update_organismo, name='organismo_edit'),
    path('eliminar_organismo/', delete_organismo, name='organismo_delete'),

    path('areatrabajo/', index_areatrabajo, name='nomenclador_areatrab'),
    path('crear_areatrabajo/', create_areatrabajo, name='areatrabajo_new'),
    path('editar_areatrabajo/', update_areatrabajo, name='areatrabajo_edit'),
    path('eliminar_areatrabajo/', delete_areatrabajo, name='areatrabajo_delete'),

    path('centrotrabajo/', index_centrotrabajo, name='nomenclador_centrab'),
    path('crear_centrotrabajo/', create_centrotrabajo, name='centrotrabajo_new'),
    path('editar_centrotrabajo/', update_centrotrabajo, name='centrotrabajo_edit'),
    path('eliminar_centrotrabajo/', delete_centrotrabajo, name='centrotrabajo_delete'),
]