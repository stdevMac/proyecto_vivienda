from django import forms
from django.contrib.auth.models import Group, User, Permission
from apps.dpv_nomencladores.models import Calle, AreaTrabajo, CentroTrabajo, Genero, Municipio


class LoginForm(forms.Form):
    username_login = forms.CharField(max_length=255, required=True, label="Nombre de usuario ó Correo electrónico", help_text="Aqui introdusca su nombre de usuario o email para entrar al sistema.",
                               widget=(forms.TextInput(attrs={"placeholder": "Nombre de usuario ó Email", "class": "form-control"})))
    password_login = forms.CharField(max_length=255, required=True, label="Contraseña",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Contraseña", "class": "form-control"})))
    remenber_me = forms.BooleanField(label="Recordarme", required=False, widget=(forms.CheckboxInput(attrs={"class": ""})))


class RecoverPassForm(forms.Form):
    username_recover = forms.CharField(max_length=255, required=True, label="Nombre de usuario ó Correo electrónico",
                               widget=(forms.TextInput(attrs={"placeholder": "Nombre de usuario ó Email", "class": "form-control"})))


class UserForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label="Nombre de Usuario", help_text="Debe ser único, no debe tener más de 30 caracteres.",
                               widget=(forms.TextInput(attrs={"placeholder": "Nombre de usuario", "class":"form-control"})))
    password = forms.CharField(max_length=255, required=True, label="Contraseña", help_text="Recuerde que la contraseña debe tener mas de 8 caracteres.\nLa contraseña debe contener letras minúsculas, mayúsculas, números y caracteres especiales.",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Contraseña", "class": "form-control"})))
    password_repeat = forms.CharField(max_length=255, required=True, label="Repetir Contraseña", help_text="Debe ser igual que la contraseña delcampo anterior.",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Repetir Contraseña", "class": "form-control"})))
    is_staff = forms.BooleanField(label="Administrador?", help_text="Marquelo para que el usuario pueda entrar al sitio de administración.",
                                       widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    first_name = forms.CharField(max_length=60, required=True, label="Nombre(s) Real(es)", help_text="Nombre real de la persona.",
                             widget=(forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"})))
    last_name = forms.CharField(max_length=100, required=True, help_text="Apellidos de la persona.",
                                widget=(forms.TextInput(attrs={"placeholder": "Apellidos", "class": "form-control"})))
    email = forms.EmailField(max_length=255, required=True, label="Correo Electrónico", help_text="Correo electronico del usuario, es al que el usuario recibira las notificaciones.",
                             widget=(forms.EmailInput(attrs={"placeholder": "Correo Electronico", "class": "form-control"})))
    permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(), label="Permisos", help_text="Permisos otorgados al usuario.",
                                                 widget=(forms.CheckboxSelectMultiple(attrs={"class": ""})))
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), label="Grupos", help_text="Grupos a los que pertenecera el usuario.\nEl usuario heredara los permisos de los grupos a los que pertenesca.",
                                            widget=(forms.CheckboxSelectMultiple(attrs={"class": ""})))


class UserProfileForm(UserForm):
    notificaciones_email = forms.BooleanField(label="Notificar a mi Correo", help_text="El usuario recibirá las notificaciones del sistema tambien por correo.",
                                              widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    documentacion_email = forms.BooleanField(label="Documentación a mi correo", help_text="El usuario recibirá la documentación del sistema a su buzon de correo",
                                             widget=(forms.CheckboxInput(attrs={"class": "form-control"})))
    area_trabajo = forms.ModelChoiceField(queryset=AreaTrabajo.objects.all(), label="Departamento", required=True, help_text="Departamento en el que trabaja el usuario",
                                     widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    centro_trabajo = forms.ModelChoiceField(queryset=CentroTrabajo.objects.all(), label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario",
                                       widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))


class FullUserForm(UserProfileForm):
    ci = forms.CharField(max_length=11, required=True, label="Número de Identidad", help_text="Número del carnet o documento de identidad.",
                         widget=(forms.TextInput(attrs={"placeholder": "CI", "class": "form-control"})))
    sexo = forms.ModelChoiceField(queryset=Genero.objects.all(), label="Sexo", required=True, help_text="Departamento en el que trabaja el usuario.",
                                     widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    movil = forms.CharField(max_length=8, label="Teléfono Movil", help_text="Teléfono movil de la persona.",
                             widget=(forms.TextInput(attrs={"placeholder": "Teléfono Movil", "class": "form-control"})))
    telefono = forms.CharField(max_length=8, label="Teléfono Fijo", help_text="Telefono fijo de la persona.",
                             widget=(forms.TextInput(attrs={"placeholder": "Teléfono Fijo", "class": "form-control"})))
    direccion_calle = forms.ModelChoiceField(queryset=Calle.objects.all(), label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario",
                                       widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    direccion_numero = forms.IntegerField(max_value=99999999, label="Número", help_text="Número de la vivienda particular del usuario.",
                                          widget=(forms.TextInput(attrs={"placeholder":"Número", "class": "form-control"})))
    direccion_entrecalle1 = forms.ModelChoiceField(queryset=Calle.objects.all(), label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario",
                                       widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    direccion_entrecalle2 = forms.ModelChoiceField(queryset=Calle.objects.all(), label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario",
                                       widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    direccion_municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario",
                                       widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', )