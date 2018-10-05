from django.contrib import admin
from .models import Municipio, Organismo, Destino, Calle, Piso, Provincia


# Register your models here.
admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Organismo)
admin.site.register(Destino)
admin.site.register(Calle)
admin.site.register(Piso)
