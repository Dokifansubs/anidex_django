from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anidex_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^refresh', 'index.views.get_stats'),
    url(r'^$', 'index.views.main'),
    url(r'^whitelist', 'index.views.whitelist'),
)
