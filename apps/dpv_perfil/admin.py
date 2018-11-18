from django.contrib import admin
from django.contrib.auth.models import User
from .models import Perfil
# from apps.dpv_perfil.forms import FullUserForm

# Register your models here.
admin.site.unregister(User)
admin.site.register(Perfil)

class UserAdmin(admin.ModelAdmin):

    list_per_page = 25
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'is_superuser', )

    # form = FullUserForm()

    fieldsets = [
        ('Datos del usuario', {'fields': ['username', 'password', 'is_active', 'is_staff', 'is_superuser', ], 'classes': ('container', 'col-md-6')}),
        # ('Datos personales', {'fields': ['first_name', 'last_name', 'ci', 'municipio', 'direccion_calle', 'direccion_numero', 'direccion_entrecalle1', 'direccion_entrecalle2', 'telefono', 'movil', 'genero', 'email'], 'classes': ('container', 'col-md-6')})
        # ('Datos del perfil', {'fields': ['noficacion_email', 'documentacion_email', ], 'classes': ('container', 'col-md-12')}),
        # ('Datos informativos', {'fields': ['date_joined', 'first_login', 'first_login_ip', ], 'classes': ('container', 'col-md-12', 'disabled')})
    ]


admin.site.register(User, UserAdmin)

