from django.conf.urls.defaults import *

from webmaps.trackit import views 

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
     (r'^$', 'webmaps.trackit.views.index'), 
     (r'map/$', 'webmaps.trackit.views.map'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
 #    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),
)
