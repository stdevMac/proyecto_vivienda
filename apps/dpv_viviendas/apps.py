from django.apps import AppConfig


class DpvViviendasConfig(AppConfig):
    name = 'apps.dpv_viviendas'       # Nombre identificador del modulo tiene que cumplir con el estandar
    verbose_name = "Viviendas"      # Nombre de Humanizado del modulo sera utilizado para mostrar en el menu
    menu = 'dpv_viviendas/menu/main_menu.html'  # Plantilla HTML de que se mostrara el modulo del menu
    menuable = True    # Si el modulo se mostrara en el menu
    owned = True        # Si es una aplicacion nuestra
    active = True       # Si el modulo esta activo, es como si esta instalado
    parent = False      # Si el modulo es un submodulo de otro en el menu (y solo en el menu)
    child_of = 'apps.dpv_locales'     # Si el modulo es hijo de otro en el menu se coloca aqui el nombre(atributo name) del modulo padre