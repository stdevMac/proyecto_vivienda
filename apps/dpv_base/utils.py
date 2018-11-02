from locales_viv import urls, settings
from django import urls as dj_urls


def store_url_names():
    settings.BULK_URLS = []
    urldo = {}
    for url_base in urls.urlpatterns:
        if isinstance(url_base, dj_urls.URLResolver):
            prefix = url_base.pattern
            for urlpattern in url_base.url_patterns:
                if isinstance(urlpattern, dj_urls.URLPattern) and urlpattern.name:
                    urldo['name'] = urlpattern.name
                    urldo['path'] = str(prefix) + '/' + str(urlpattern.pattern)
                    settings.BULK_URLS.append(urldo)
        elif isinstance(url_base, dj_urls.URLPattern):
            urldo['name'] = urlpattern.name
            urldo['path'] = urlpattern.pattern
            settings.BULK_URLS.append(urldo)
