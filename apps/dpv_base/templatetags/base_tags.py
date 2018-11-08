from django.apps import apps as all_apps
# from django.templates.defaultfilters import register, stringfilter
from django import template
from locales_viv import settings

register = template.Library()

@register.simple_tag
def local_apps():
    local_apps = []
    if all_apps.get_app_configs:
        for app in all_apps.get_app_configs():
            if hasattr(app, 'owned') and app.active:
                local_apps.append(app)
    return local_apps

@register.simple_tag
def menuable_apps():
    menuable_apps = []
    if all_apps.get_app_configs:
        for app in all_apps.get_app_configs():
            if hasattr(app, 'owned') and app.active:
                if hasattr(app, 'menuable'):
                    menuable_apps.append(app)
    return menuable_apps

@register.simple_tag()
def exist_url(url=None):
    if not url:
        return False
    return url in settings.BULK_URLS

@register.simple_tag()
def ative_url(url=None):
    if not url:
        return False
    for urlpath in settings.BULK_URLS:
        pass

