from django import forms
from django.contrib.auth.models import Group, User
from apps.dpv_nomencladores.models import Calle, AreaTrabajo, CentroTrabajo, Genero


class LoginForm(forms.Form):
    username_login = forms.CharField(max_length=255, required=True, label="Nombre de usuario ó Correo electrónico", help_text="Aqui introdusca su nombre de usuario o email para entrar al sistema.",
                               widget=(forms.TextInput(attrs={"placeholder": "Nombre de usuario ó Email", "class": "form-control"})))
    password_login = forms.CharField(max_length=255, required=True, label="Contraseña",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Contraseña", "class": "form-control"})))
    remenber_me = forms.BooleanField(label="Recordarme", required=False, widget=(forms.CheckboxInput(attrs={"class": ""})))


class RecoverPassForm(forms.Form):
    username_recover = forms.CharField(max_length=255, required=True, label="Nombre de usuario ó Correo electrónico",
                               widget=(forms.TextInput(attrs={"placeholder": "Nombre de usuario ó Email", "class": "form-control"})))
    

class FullUserForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label="Nombre de Usuario", help_text="Debe ser único, no debe tener más de 30 caracteres.",
                               widget=(forms.TextInput(attrs={"placeholder": "Nombre de usuario", "class":"form-control"})))
    password = forms.CharField(max_length=255, required=True, label="Contraseña", help_text="Recuerde que la contraseña debe tener mas de 8 caracteres.\nLa contraseña debe contener letras minúsculas, mayúsculas, números y caracteres especiales.",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Contraseña", "class": "form-control"})))   
    password_repeat = forms.CharField(max_length=255, required=True, label="Repetir Contraseña", help_text="Debe ser igual que la contraseña delcampo anterior.",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Repetir Contraseña", "class": "form-control"})))
    administrador = forms.BooleanField(label="Administrador?", help_text="Marquelo para que el usuario pueda entrar al sitio de administración.",
                                       widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    notificaciones_email = forms.BooleanField(label="Notificar a mi Correo", help_text="El usuario recibirá las notificaciones del sistema tambien por correo.",
                                              widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    documentacion_email = forms.BooleanField(label="Documentación a mi correo", help_text="El usuario recibirá la documentación del sistema a su buzon de correo.",
                                             widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    # area_trabajo = forms.ChoiceField(label="Departamento", required=True, help_text="Departamento en el que trabaja el usuario.", choices=AreaTrabajo.objects.all(),
    #                                  widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    # centro_trabajo = forms.ChoiceField(label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario", choices=CentroTrabajo.objects.all(),
    #                                    widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    ci = forms.CharField(max_length=11, required=True, label="Número de Identidad", help_text="Número del carnet o documento de identidad.",
                         widget=(forms.TextInput(attrs={"placeholder": "CI", "class": "form-control"})))
    # sexo = forms.ChoiceField(label="Departamento", required=True, help_text="Departamento en el que trabaja el usuario.", choices=Genero.objects.all(),
    #                                  widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    nombre = forms.CharField(max_length=60, required=True, label="Nombre(s) Real(es)", help_text="Nombre real de la persona.",
                             widget=(forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"})))
    apellidos = forms.CharField(max_length=100, required=True, help_text="Apellidos de la persona.",
                                widget=(forms.TextInput(attrs={"placeholder": "Apellidos", "class": "form-control"})))
    email = forms.EmailField(max_length=255, required=True, label="Correo Electrónico", help_text="Correo electronico del usuario, es al que el usuario recibira las notificaciones.",
                             widget=(forms.EmailInput(attrs={"placeholder": "Correo Electronico", "class": "form-control"})))
    movil = forms.CharField(max_length=8, label="Teléfono Movil", help_text="Teléfono movil de la persona.",
                             widget=(forms.TextInput(attrs={"placeholder": "Teléfono Movil", "class": "form-control"})))
    telefono = forms.CharField(max_length=8, label="Teléfono Fijo", help_text="Telefono fijo de la persona.",
                             widget=(forms.TextInput(attrs={"placeholder": "Teléfono Fijo", "class": "form-control"})))
    # direccion_calle = forms.ChoiceField(label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario", choices=Calle.objects.all(),
    #                                    widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    direccion_numero = forms.IntegerField(max_value=99999999, label="Número", help_text="Número de la vivienda particular del usuario.",
                                          widget=(forms.TextInput(attrs={"placeholder":"Número", "class": "form-control"})))
    # direccion_entrecalle1 = forms.ChoiceField(label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario", choices=Calle.objects.all(),
    #                                    widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    # direccion_entrecalle2 = forms.ChoiceField(label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario", choices=Calle.objects.all(),
    #                                    widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    # direccion_municipio = forms.ChoiceField(label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario", choices=Calle.objects.all(),
    #                                    widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))

    def clean(self):
        pass


class UserProfileForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label="Nombre de Usuario", help_text="Debe ser único, no debe tener más de 30 caracteres.",
                               widget=(forms.TextInput(attrs={"placeholder": "Nombre de usuario", "class":"form-control"})))
    password = forms.CharField(max_length=255, required=True, label="Contraseña", help_text="Recuerde que la contraseña debe tener mas de 8 caracteres.\nLa contraseña debe contener letras minúsculas, mayúsculas, números y caracteres especiales.",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Contraseña", "class": "form-control"})))
    password_repeat = forms.CharField(max_length=255, required=True, label="Repetir Contraseña", help_text="Debe ser igual que la contraseña delcampo anterior.",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Repetir Contraseña", "class": "form-control"})))
    administrador = forms.BooleanField(label="Administrador?", help_text="Marquelo para que el usuario pueda entrar al sitio de administración.",
                                       widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    notificaciones_email = forms.BooleanField(label="Notificar a mi Correo", help_text="El usuario recibirá las notificaciones del sistema tambien por correo.",
                                              widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    documentacion_email = forms.BooleanField(label="Documentación a mi correo", help_text="El usuario recibirá la documentación del sistema a su buzon de correo",
                                             widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    # area_trabajo = forms.ChoiceField(label="Departamento", required=True, help_text="Departamento en el que trabaja el usuario", choices=AreaTrabajo.objects.all(),
    #                                  widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    #
    # centro_trabajo = forms.ChoiceField(label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario", choices=CentroTrabajo.objects.all(),
    #                                    widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))

    nombre = forms.CharField(max_length=60, required=True, label="Nombre(s) Real(es)", help_text="Nombre real de la persona",
                             widget=(forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"})))
    apellidos = forms.CharField(max_length=100, required=True, help_text="Apellidos de la persona",
                                widget=(forms.TextInput(attrs={"placeholder": "Apellidos", "class": "form-control"})))
    email = forms.EmailField(max_length=255, required=True, label="Correo Electrónico", help_text="Correo electronico del usuario, es al que el usuario recibira las notificaciones.",
                             widget=(forms.EmailInput(attrs={"placeholder": "Correo Electronico", "class": "form-control"})))


class UserForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label="Nombre de Usuario", help_text="Debe ser único, no debe tener más de 30 caracteres.",
                               widget=(forms.TextInput(attrs={"placeholder": "Nombre de usuario", "class":"form-control"})))
    password = forms.CharField(max_length=255, required=True, label="Contraseña", help_text="Recuerde que la contraseña debe tener mas de 8 caracteres.\nLa contraseña debe contener letras minúsculas, mayúsculas, números y caracteres especiales.",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Contraseña", "class": "form-control"})))
    password_repeat = forms.CharField(max_length=255, required=True, label="Repetir Contraseña", help_text="Debe ser igual que la contraseña delcampo anterior.",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Repetir Contraseña", "class": "form-control"})))
    administrador = forms.BooleanField(label="Administrador?", help_text="Marquelo para que el usuario pueda entrar al sitio de administración.",
                                       widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    nombre = forms.CharField(max_length=60, required=True, label="Nombre(s) Real(es)", help_text="Nombre real de la persona.",
                             widget=(forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"})))
    apellidos = forms.CharField(max_length=100, required=True, help_text="Apellidos de la persona.",
                                widget=(forms.TextInput(attrs={"placeholder": "Apellidos", "class": "form-control"})))
    email = forms.EmailField(max_length=255, required=True, label="Correo Electrónico", help_text="Correo electronico del usuario, es al que el usuario recibira las notificaciones.",
                             widget=(forms.EmailInput(attrs={"placeholder": "Correo Electronico", "class": "form-control"})))


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', ]