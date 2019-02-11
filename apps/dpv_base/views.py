from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.db.models import Q
from .forms import LoginForm, RecoverPassForm
from django.utils.translation import ugettext as _
from .forms import FullUserForm, UserProfileForm, UserForm
from django.apps import apps as all_apps
from locales_viv import settings
from .utils import store_url_names
from locales_viv import urls


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
def users_add(request):
    exist_perfil = False
    exist_persona = False
    form = UserForm()
    if all_apps.get_app_configs():
        for app in all_apps.get_app_configs():
            if 'dpv_perfil' in app.label:
                exist_perfil = True
            if 'dpv_persona' in app.label:
                exist_persona = True
    if exist_perfil:
        form = UserProfileForm
    if exist_persona and exist_perfil:
        form = FullUserForm
    return render(request, 'layouts/admin/users_form.html', {'form': form})


@permission_required('auth.view_group', raise_exception=True)
def users_view(request):
    usuarios = User.objects.all()
    return render(request, 'layouts/admin/users.html', {'usuarios': usuarios})


@permission_required('auth.view_logentry', raise_exception=True)
def logs_view(request):
    pass