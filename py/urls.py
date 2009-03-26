from django.conf.urls.defaults import *

from py.buildmeabikerack import views 

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    (r'^$', 'py.buildmeabikerack.views.index'), 
    (r'^rack/(?P<rack_id>\d+)/$', 'py.buildmeabikerack.views.rack'),                        
   
    (r'rack/all.kml$', 'py.buildmeabikerack.views.rack_all_kml'),
    (r'rack/(?P<rack_id>\d+).kml', 'py.buildmeabikerack.views.rack_all_kml'),
    (r'^rack/new/$', 'py.buildmeabikerack.views.newrack'), 

                       
    (r'^neighborhoods/$', 'py.buildmeabikerack.views.neighborhoods'), 


#    (r'^@api/rack/$','py.buildmeabikerack.views.api_newrack'), 


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
 #    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),
)
