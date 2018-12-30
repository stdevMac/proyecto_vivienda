from django.shortcuts import render, redirect
from apps.email_sender.forms import ConfigureMailForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.utils.translation import ugettext as _
from django.apps import apps as all_apps
from .forms import LoginForm, RecoverPassForm
from .forms import FullUserForm, UserProfileForm, UserForm, GroupForm, UserMForm
from .utils import store_url_names
from apps.dpv_persona.models import PersonaNatural
from apps.dpv_persona.forms import PersonaNaturalMForm
from apps.dpv_perfil.models import Perfil
from apps.dpv_perfil.forms import PerfilMForm
from apps.email_sender.models import EmailConfigurate


# Create your views here.
@login_required()
def index(request):
    return render(request, 'layouts/dashboard.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('base_dashboard'))
    else:
        store_url_names()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                user_pass = form_data.get('password_login')
                user_name = form_data.get('username_login')
                not_expiry = form_data.get('remenber_me')
                user = User.objects.filter(Q(email=user_name) | Q(username=user_name)).first()
                if user and user.is_active:
                    if user.is_authenticated:
                        form.add_error('username_login', _('Ese usuario ya se encuetra logueado.'))
                    access = authenticate(username=user.username, password=user_pass)
                    if access:
                        login(request, access)
                        if not_expiry:
                            request.session.set_expiry(4838400)
                        return redirect(reverse_lazy('base_dashboard'))
                    else:
                        form.add_error('username_login', _('Combinación no válida de usuario y contraseña'))
                else:
                    form.add_error('username_login', _('Ese usuario no exitse o está incativo contacte con el administrador del sistema'))
            else:
                form.add_error('username_login', _('Error de usuario o contraseña no valido'))
            return render(request, 'layouts/login.html', { 'form': form })
        else:
            form = LoginForm()
            return render(request, 'layouts/login.html', { 'form': form })


def recover_pass_page(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('base_dashboard'))
    else:
        if request.method == 'POST':
            pass
        else:
            form = RecoverPassForm
            return render(request, 'layouts/recoverpass.html', {'form': form})

    return render(request, 'layouts/recoverpass.html')


@login_required
def logout_page(request):
    logout(request)
    return redirect(reverse_lazy('base_login'))


@permission_required('auth.view_user', raise_exception=True)
def groups_view(request):
    grupos = Group.objects.all()
    return render(request, 'layouts/admin/groups.html', {'grupos': grupos})


@permission_required('auth.add_user', raise_exception=True)
def user_add(request):
    exist_perfil = False
    exist_persona = False
    if all_apps.get_app_configs():
        for app in all_apps.get_app_configs():
            if 'dpv_perfil' in app.label:
                exist_perfil = True
            if 'dpv_persona' in app.label:
                exist_persona = True
    if request.method == 'POST':
        form = UserMForm(request.POST)
        if exist_persona:
            formprs = PersonaNaturalMForm(request.POST)
        if exist_perfil:
            formprf = PerfilMForm(request.POST)
        print("hay que validar")
        if form.is_valid() and formprs.is_valid():
            print("to esta valido sin validar perfil")
            usr = form.save()
            prs = formprs.save()
            prs.nombre = usr.first_name
            prs.apellidos = usr.last_name
            prs.save()
            formprf.datos_usuario = usr.id
            formprf.datos_personales = prs.id
            print("a validar perfil")
            if formprf.is_valid():
                print("perfil validao y salvo")
                formprf.save()
            else:
                print("ese invento no pincho")
                usr.delete()
                prs.delete()
                return render(request, 'layouts/admin/users_form.html', {'form': form, 'formprs': formprs, 'formprf': formprf })
            return redirect('admin_user')
        else:
            return render(request, 'layouts/admin/users_form.html', {'form': form, 'formprs': formprs, 'formprf': formprf })
    else:
        form = UserMForm()
        if exist_persona:
            formprs = PersonaNaturalMForm()
        if exist_perfil:
            formprf = PerfilMForm()
    return render(request, 'layouts/admin/users_form.html', {'form': form, 'formprs': formprs, 'formprf': formprf })




@permission_required('auth.add_group', raise_exception=True)
def group_add(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_group')
        else:
            return render(request, 'layouts/admin/groups_form.html', {'form': form})
    else:
        form = GroupForm()
        return render(request, 'layouts/admin/groups_form.html', {'form': form})


@permission_required('auth.view_group', raise_exception=True)
def users_view(request):
    usuarios = User.objects.none()
    try:
        perfil = request.user.perfil_usuario
        try:
            ct = perfil.centro_trabajo
            if ct.oc:
                usuarios = User.objects.all().exclude(is_superuser=True)
            else:
                usuarios = User.objects.filter(perfil_usuario__centro_trabajo=request.user.perfil_usuario.centro_trabajo).exclude(is_superuser=True)
        except:
            print("no tiene centro de trabajo asociado")
    except:
        print("no tiene perfil asociado")
    return render(request, 'layouts/admin/users.html', {'usuarios': usuarios})


@permission_required('auth.view_logentry', raise_exception=True)
def logs_view(request):
    pass


@permission_required('email_sender.add_emailconfigurate', raise_exception=True)
def configure_email(request):
    ec = EmailConfigurate.objects.all().first()
    if request.method == 'POST':
        form = ConfigureMailForm(request.POST, instance=ec)
        if form.is_valid():
            form.save()
            return render(request, 'layouts/admin/mailconf.html', {'form': form, 'ec': ec})
        else:
            return render(request, 'layouts/admin/mailconf.html', {'form': form, 'ec': ec})
    else:
        form = ConfigureMailForm(instance=ec)
        return render(request, 'layouts/admin/mailconf.html', {'form': form, 'ec': ec})


@permission_required('auth.change_user', raise_exception=True)
def user_edit(request, id_user):
    usr = User.objects.filter(id=id_user).first()
    prf = Perfil.objects.filter(datos_usuario=usr.id).first()
    prs = PersonaNatural.objects.filter(id=prf.datos_personales).first()
    if request.method == 'POST':
        form = UserMForm(request.POST, instance=usr)
        formprs = PersonaNaturalMForm(request.POST, instance=prs)
        formprf = PerfilMForm(request.POST, instance=prf)
        if form.is_valid() and formprf.is_valid() and formprs.is_valid():
            form.save()
            formprs.save()
            formprf.save()
            return redirect(reverse_lazy('admin_user'))
    return render(request, 'layouts/admin/users_form.html', {'form': form, 'formprs': formprs, 'formprf': formprf})


@permission_required('auth.change_group', raise_exception=True)
def group_edit(request, id_group):
    grp = Group.objects.filter(id=id_group).first()
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=grp)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('admin_group'))
    else:
        form = GroupForm(instance=grp)
    return render(request, 'layouts/admin/groups_form.html', {'form': form})
