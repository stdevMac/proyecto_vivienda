from django.contrib import admin
from django.urls import path, include
from apps.dpv_base import urls as base_url
from apps.dpv_nomencladores import urls as nomencladores_url
from apps.dpv_locales import urls as locales_url
from apps.dpv_persona import urls as persona_url
from apps.dpv_perfil import urls as perfil_url
from apps.dpv_viviendas import urls as vivienda_url
from apps.dpv_complaint import urls as complaint_url
from apps.dpv_events import urls as events_url
from apps.email_sender import urls as email_url


urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('', include(base_url)),
    path('nomenclador/', include(nomencladores_url)),
    path('local/', include(locales_url)),
    path('persona/', include(persona_url)),
    path('perfil/', include(perfil_url)),
    path('vivienda/', include(vivienda_url)),
    path('quejas/', include(complaint_url)),
    path('dpv_events/', include(events_url)),
    path('emailing/', include(email_url)),
]
