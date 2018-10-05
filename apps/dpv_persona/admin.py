from django.contrib import admin
from .models import PersonaNatural, Genero, CentroTrabajo, AreaTrabajo, PersonaJuridica

# Register your models here.
admin.site.register(PersonaNatural)
admin.site.register(PersonaJuridica)
admin.site.register(Genero)
admin.site.register(CentroTrabajo)
admin.site.register(AreaTrabajo)
