from locales_viv import urls, settings
from django import urls as dj_urls
from .models import ConfigMail
import os, sys


def store_url_names():
    settings.BULK_URLS = []
    for url_base in urls.urlpatterns:
        if isinstance(url_base, dj_urls.URLResolver):
            for urlpattern in url_base.url_patterns:
                if isinstance(urlpattern, dj_urls.URLPattern) and urlpattern.name:
                    settings.BULK_URLS.append(urlpattern.name)
        elif isinstance(url_base, dj_urls.URLPattern):
            settings.BULK_URLS.append(url_base.name)


def get_settings_email_conf():
    conf = ConfigMail()
    conf.password = settings.EMAIL_HOST_PASSWORD or ''
    conf.usuario = settings.EMAIL_HOST_USER or ''
    conf.servidor = settings.EMAIL_HOST or ''
    conf.puerto = settings.EMAIL_PORT or ''
    conf.use_tls = settings.EMAIL_USE_TLS or False
    conf.use_ssl = settings.EMAIL_USE_SSL or False
    return conf


def get_db_email_conf():
    conf = ConfigMail.objects.all().first()
    return conf


def comapare_db_settings_conf(confdb, confset):
    return confdb.usuario == confset.usuario and confdb.servidor == confset.servidor and int(confdb.puerto) == int(confset.puerto) and confdb.password == confset.password and confdb.use_tls == confset.use_tls and confdb.use_ssl == confset.use_ssl


def set_settings_email_conf(configuration):
    if not configuration:
        return
    print(dir(configuration))
    if configuration.use_ssl and configuration.use_tls:
        configuration.use_ssl = False
        configuration.use_tls = False
    try:
        settingdfile = open(os.path.join(settings.BASE_DIR, 'locales_viv/settings.py'), "r", encoding="utf-8")
        lines = settingdfile.readlines()
        settingdfile.close()
    except:
        print("no se pudo abrir el archivo para leerlo")
    # for line in lines:
    #     if 'EMAIL_HOST ' in line:
    #         lines.remove(line)
    #         new_line = 'EMAIL_HOST = "' + str(configuration.servidor) + '"\n'
    #         lines.append(new_line)
    #         print("entre host")
    #     if 'EMAIL_HOST_PASSWORD ' in line:
    #         # lines.remove(line)
    #         new_line = 'EMAIL_HOST_PASSWORD = "' + str(configuration.password) + '"\n'
    #         # new_line = 'EMAIL_HOST_PASSWORD = "password"\n'
    #         lines.append(new_line)
    #         print("entre pass")
    #     if 'EMAIL_HOST_USER ' in line:
    #         # lines.remove(line)
    #         new_line = 'EMAIL_HOST_USER = "' + str(configuration.usuario) + '"\n'
    #         # new_line = 'EMAIL_HOST_USER = "usermanual"\n'
    #         lines.append(new_line)
    #         print("entre user")
    #     if 'EMAIL_PORT ' in line:
    #         # lines.remove(line)
    #         new_line = 'EMAIL_PORT = "' + str(configuration.puerto) + '"\n'
    #         # new_line = 'EMAIL_PORT = "8000"\n'
    #         lines.append(new_line)
    #         print("entre port")
    #     if 'EMAIL_USE_TLS ' in line:
    #         # lines.remove(line)
    #         new_line = 'EMAIL_USE_TLS = ' + str(configuration.use_tls) + '\n'
    #         # new_line = 'EMAIL_USE_TLS = True\n'
    #         lines.append(new_line)
    #         print("entre tls")
    #     if 'EMAIL_USE_SSL ' in line:
    #         # lines.remove(line)
    #         new_line = 'EMAIL_USE_SSL = ' + str(configuration.use_ssl) + '\n'
    #         # new_line = 'EMAIL_USE_SSL = True\n'
    #         lines.append(new_line)
    #         print("entre ssl")
    try:
        settingdfile = open(os.path.join(settings.BASE_DIR, 'locales_viv/settings.py'), "w", encoding="utf-8")
    except:
        print("no se pudo escribir en el archivo")
    else:
        #settingdfile.writelines(lines)
        for line in lines:
            if 'EMAIL_HOST ' in line:
                new_line = 'EMAIL_HOST = "' + str(configuration.servidor) + '"\n'
                settingdfile.write(new_line)
            elif 'EMAIL_HOST_PASSWORD ' in line:
                new_line = 'EMAIL_HOST_PASSWORD = "' + str(configuration.password) + '"\n'
                settingdfile.write(new_line)
            elif 'EMAIL_HOST_USER ' in line:
                new_line = 'EMAIL_HOST_USER = "' + str(configuration.usuario) + '"\n'
                settingdfile.write(new_line)
            elif 'EMAIL_PORT ' in line:
                new_line = 'EMAIL_PORT = "' + str(configuration.puerto) + '"\n'
                settingdfile.write(new_line)
            elif 'EMAIL_USE_TLS ' in line:
                new_line = 'EMAIL_USE_TLS = ' + str(configuration.use_tls) + '\n'
                settingdfile.write(new_line)
            elif 'EMAIL_USE_SSL ' in line:
                new_line = 'EMAIL_USE_SSL = ' + str(configuration.use_ssl) + '\n'
                settingdfile.write(new_line)
            else:
                settingdfile.write(line)
        settingdfile.close()
    return True


def main_email_candy_conf(db_config=None):
    settings_conf = get_settings_email_conf()
    if not db_config:
        db_config = get_db_email_conf()
    same_config = comapare_db_settings_conf(db_config, settings_conf)
    if not same_config:
        set_ok = set_settings_email_conf(db_config)


