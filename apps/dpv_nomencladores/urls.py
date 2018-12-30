from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='nomenclador_index'),

    path('provincia/', index_provincia, name='nomenclador_provincia'),
    path('nueva_provincia/', add_provincia, name='provincia_new'),
    path('editar_provincia/<int:id_provincia>', update_provincia, name='provincia_edit'),
    path('eliminar_provincia/<int:id_provincia>', delete_provincia, name='provincia_delete'),

    path('municipio/', index_municipio, name='nomenclador_municipio'),
    path('nuevo_municipio/', add_municipio, name='municipio_new'),
    path('editar_municipio/<int:id_municipio>', update_municipio, name='municipio_edit'),
    path('eliminar_municipio/<int:id_municipio>', delete_municipio, name='municipio_delete'),

    path('consejopopular/', index_consejopopular, name='nomenclador_consejopopular'),
    path('nuevo_consejopopular/', add_consejopopular, name='consejopopular_new'),
    path('editar_consejopopular/<int:id_consejopopular>', update_consejopopular, name='consejopopular_edit'),
    path('eliminar_consejopopular/<int:id_consejopopular>', delete_consejopopular, name='consejopopular_delete'),

    path('calle/', index_calle, name='nomenclador_calle'),
    path('nueva_calle/', add_calle, name='calle_new'),
    path('editar_calle/<int:id_calle>', update_calle, name='calle_edit'),
    path('eliminar_calle/<int:id_calle>', delete_calle, name='calle_delete'),

    path('piso/', index_piso, name='nomenclador_piso'),
    path('nuevo_piso/', add_piso, name='piso_new'),
    path('editar_piso/<int:id_piso>', update_piso, name='piso_edit'),
    path('eliminar_piso/<int:id_piso>', delete_piso, name='piso_delete'),

    path('organismo/', index_organismo, name='nomenclador_organismo'),
    path('nuevo_organismo/', add_organismo, name='organismo_new'),
    path('editar_organismo/<int:id_organismo>', update_organismo, name='organismo_edit'),
    path('eliminar_organismo/<int:id_organismo>', delete_organismo, name='organismo_delete'),

    path('destino/', index_destino, name='nomenclador_destino'),
    path('nuevo_destino/', add_destino, name='destino_new'),
    path('editar_destino/<int:id_destino>', update_destino, name='destino_edit'),
    path('eliminar_destino/<int:id_destino>', delete_destino, name='destino_delete'),

    path('concepto/', index_concepto, name='nomenclador_concepto'),
    path('nuevo_concepto/', add_concepto, name='concepto_new'),
    path('editar_concepto/<int:id_concepto>', update_concepto, name='concepto_edit'),
    path('eliminar_concepto/<int:id_concepto>', delete_concepto, name='concepto_delete'),

    path('genero/', index_genero, name='nomenclador_genero'),
    path('nuevo_genero/', add_genero, name='genero_new'),
    path('editar_genero/<int:id_genero>/', update_genero, name='genero_edit'),
    path('eliminar_genero/<int:id_genero>', delete_genero, name='genero_delete'),

    path('departamento/', index_areatrabajo, name='nomenclador_areatrab'),
    path('nuevo_departamento/', add_areatrabajo, name='areatrabajo_new'),
    path('editar_departamento/<int:id_areatrabajo>', update_areatrabajo, name='areatrabajo_edit'),
    path('eliminar_departamento/<int:id_areatrabajo>', delete_areatrabajo, name='areatrabajo_delete'),

    path('unidad/', index_centrotrabajo, name='nomenclador_centrab'),
    path('nuevo_centrotrabajo/', add_centrotrabajo, name='centrotrabajo_new'),
    path('editar_unidad/<int:id_centrotrabajo>', update_centrotrabajo, name='centrotrabajo_edit'),
    path('eliminar_unidad/<int:id_centrotrabajo>', delete_centrotrabajo, name='centrotrabajo_delete'),
]