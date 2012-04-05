from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pidgin_post_handler.views.home', name='home'),
    # url(r'^pidgin_post_handler/', include('pidgin_post_handler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Add URLS from stats collector app

    # Nice simple, home page
    url(r'^collectstats/$', 'statscollector.views.index'),

    # Accepts a GET reuqest to process
    url(r'^collectstats/collect/$', 'statscollector.views.collect'),
)
