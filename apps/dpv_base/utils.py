from locales_viv import urls, settings
from django import urls as dj_urls


def store_url_names():
    settings.BULK_URLS = []
    for url_base in urls.urlpatterns:
        if isinstance(url_base, dj_urls.URLResolver):
            for urlpattern in url_base.url_patterns:
                if isinstance(urlpattern, dj_urls.URLPattern) and urlpattern.name:
                    settings.BULK_URLS.append(urlpattern.name)
        elif isinstance(url_base, dj_urls.URLPattern):
            settings.BULK_URLS.append(url_base.name)
