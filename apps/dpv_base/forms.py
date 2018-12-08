from django import forms
from django.db.models import Q
from django.contrib.auth.models import Group, User, Permission
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator, EmailValidator, URLValidator
from apps.dpv_nomencladores.models import Calle, AreaTrabajo, CentroTrabajo, Genero, Municipio
from apps.dpv_nomencladores.validators import only_letters, only_numbers
from apps.dpv_persona.validators import ci_validate
from .models import ConfigMail
from .Widgets import DivCheckboxSelectMultiple


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
                               widget=(forms.TextInput(attrs={"placeholder": "Nombre de usuario", "class":"form-control"})),
                               validators=[MaxLengthValidator(50)])
    email = forms.EmailField(max_length=255, required=True, label="Correo Electrónico", help_text="Correo electronico del usuario, es al que el usuario recibira las notificaciones.",
                             widget=(forms.EmailInput(attrs={"placeholder": "Correo Electronico", "class": "form-control"})),
                             validators=[MaxLengthValidator(255), EmailValidator()])
    password = forms.CharField(max_length=255, required=True, label="Contraseña", help_text="Recuerde que la contraseña debe tener mas de 8 caracteres.\nLa contraseña debe contener letras minúsculas, mayúsculas, números y caracteres especiales.",
                               widget=(forms.PasswordInput(attrs={"placeholder": "Contraseña", "class": "form-control"})),
                               validators=[MaxLengthValidator(255), MinLengthValidator(8)])
    password_repeat = forms.CharField(max_length=255, required=True, label="Repetir Contraseña", help_text="Debe ser igual que la contraseña del campo anterior.",
                                     widget=(forms.PasswordInput(attrs={"placeholder": "Repetir Contraseña", "class": "form-control"})))
    first_name = forms.CharField(max_length=60, required=True, label="Nombre(s) Real(es)", help_text="Nombre real de la persona.",
                                 widget=(forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"})),
                                 validators=[MaxLengthValidator(60), MinLengthValidator(2), only_letters])
    last_name = forms.CharField(max_length=100, label="Apellidos", required=True, help_text="Apellidos de la persona.",
                                widget=(forms.TextInput(attrs={"placeholder": "Apellidos", "class": "form-control"})),
                                validators=[MaxLengthValidator(100), MinLengthValidator(10), only_letters])
    permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(), required=False, label="Permisos",  help_text="Permisos otorgados al usuario.",
                                                 widget=(DivCheckboxSelectMultiple(attrs={"class": "form-control multi-select-box"})))
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False, label="Grupos", help_text="Grupos a los que pertenecera el usuario.\nEl usuario heredara los permisos de los grupos a los que pertenesca.",
                                            widget=(DivCheckboxSelectMultiple(attrs={"class": "form-control multi-select-box" })))
    is_staff = forms.BooleanField(label="Administrador", required=False, help_text="Marquelo para que el usuario pueda entrar al sitio de administración.",
                                  widget=(forms.CheckboxInput(attrs={"class": "form-check-input"})))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        repeated = self.cleaned_data.get('password_repeat')
        if password != repeated:
            raise ValidationError('Las contraseñas no coinciden.', code='distinct_password_and_repeated')
        return  self.cleaned_data.get('password')


class UserProfileForm(UserForm):
    notificaciones_email = forms.BooleanField(label="Notificar a mi Correo", required=False, help_text="El usuario recibirá las notificaciones del sistema tambien por correo.",
                                              widget=(forms.CheckboxInput(attrs={"class": "form-check-input"})))
    documentacion_email = forms.BooleanField(label="Documentación a mi correo", required=False, help_text="El usuario recibirá la documentación del sistema a su buzon de correo",
                                             widget=(forms.CheckboxInput(attrs={"class": "form-check-input"})))
    area_trabajo = forms.ModelChoiceField(queryset=AreaTrabajo.objects.all(), label="Departamento", required=True, help_text="Departamento en el que trabaja el usuario",
                                     widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    centro_trabajo = forms.ModelChoiceField(queryset=CentroTrabajo.objects.all(), label="Unidad", required=True, help_text="Unidad en la que trabaja el usuario",
                                       widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))


class FullUserForm(UserProfileForm):
    ci = forms.CharField(max_length=11, required=True, label="Número de Identidad", help_text="Número del carnet o documento de identidad.",
                         widget=(forms.TextInput(attrs={"placeholder": "CI", "class": "form-control"})),
                         validators=[MaxLengthValidator(11), MinLengthValidator(11), only_numbers, ci_validate])
    sexo = forms.ModelChoiceField(queryset=Genero.objects.all(), label="Sexo", required=True, help_text="Departamento en el que trabaja el usuario.",
                                  widget=(forms.Select(attrs={"placeholder": "Seleccione un Depto.", "class": "form-control"})))
    movil = forms.CharField(max_length=8, label="Teléfono Movil", help_text="Teléfono movil de la persona.",
                            widget=(forms.TextInput(attrs={"placeholder": "Teléfono Movil", "class": "form-control"})),
                            validators=[MinLengthValidator(8),MaxLengthValidator(8), only_numbers])
    telefono = forms.CharField(max_length=8, label="Teléfono Fijo", help_text="Telefono fijo de la persona.",
                               widget=(forms.TextInput(attrs={"placeholder": "Teléfono Fijo", "class": "form-control"})),
                               validators=[MaxLengthValidator(8), MinLengthValidator(8), only_numbers])
    direccion_calle = forms.ModelChoiceField(queryset=Calle.objects.all(), label="Calle", required=True, help_text="Calle de la dirección de la persona",
                                             widget=(forms.Select(attrs={"placeholder": "Seleccione una Calle.", "class": "form-control"})))
    direccion_numero = forms.IntegerField(max_value=999999, label="Número", help_text="Número de la vivienda particular del usuario.",
                                          widget=(forms.TextInput(attrs={"placeholder":"Número", "class": "form-control"})),
                                          validators=[MinValueValidator(1), MaxValueValidator(999999)])
    direccion_entrecalle1 = forms.ModelChoiceField(queryset=Calle.objects.all(), label="Primera entre calle", required=True, help_text="Primera entre calle de la dirección",
                                                   widget=(forms.Select(attrs={"placeholder": "Seleccione una Calle.", "class": "form-control"})))
    direccion_entrecalle2 = forms.ModelChoiceField(queryset=Calle.objects.all(), label="Segunda entre calle", required=True, help_text="Segunda entre calle de la dirección",
                                                   widget=(forms.Select(attrs={"placeholder": "Seleccione uns Calle", "class": "form-control"})))
    direccion_municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), label="Municipio", required=True, help_text="Municipio donde recide la persona",
                                                   widget=(forms.Select(attrs={"placeholder": "Seleccione un Municipio", "class": "form-control"})))

    def clean_telefono(self):
        movil = self.cleaned_data.get('movil')
        telefono = self.cleaned_data.get('telefono')
        if movil == telefono:
            print("netro")
            raise ValidationError('Los teléfonos no pueden ser iguales.', code='same_phone')
        return self.cleaned_data.get('movil')

    def clean_direccion_calle(self):
        calle = self.cleaned_data.get('direccion_calle')
        entre1 = self.data.get('direccion_entrecalle1')
        entre2 = self.data.get('direccion_entrecalle2')
        entrecalles = Calle.objects.filter(Q(id=entre1) | Q(id=entre2))
        if calle in entrecalles:
            raise ValidationError('La Calle no puede ser igual a ninguna de las entre calles.', code='same_street')
        return self.cleaned_data

    def clean_direccion_entrecalle1(self):
        entrecalle1 = self.cleaned_data.get('direccion_entrecalle1')
        entrecalle2 = self.data.get('direccion_entrecalle2')
        entre2 = Calle.objects.filter(id=entrecalle2)
        if entrecalle1 in entre2:
            raise ValidationError('Las entre calles no pueden ser iguales', code='betewnstreet_equals')
        return self.cleaned_data.get('direccion_entrecalle1')


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'permissions')
        widgets = {
            'permissions': DivCheckboxSelectMultiple(attrs={"class": "form-control multi-select-box" }),
        }


class ConfigMail(forms.ModelForm):
    class Meta:
        model = ConfigMail
        fields = ('servidor', 'puerto', 'usuario', 'password', 'usa_tls', 'usa_ssl', )
