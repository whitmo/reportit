from django.conf.urls.defaults import *

from bmabr.buildmeabikerack import views 

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    (r'^$', 'bmabr.buildmeabikerack.views.index'), 
    (r'^rack/(?P<rack_id>\d+)/$', 'bmabr.buildmeabikerack.views.rack'),                        
   

     # KML URL 

    (r'rack/all.kml$', 'bmabr.buildmeabikerack.views.rack_all_kml'),
    (r'rack/requested.kml$', 'bmabr.buildmeabikerack.views.rack_requested_kml'),
    (r'rack/pendding.kml$', 'bmabr.buildmeabikerack.views.rack_pendding_kml'),
    (r'rack/built.kml$', 'bmabr.buildmeabikerack.views.rack_pendding_kml'),

    (r'rack/(?P<rack_id>\d+).kml', 'bmabr.buildmeabikerack.views.rack_by_id_kml'),

    (r'^rack/new/$', 'bmabr.buildmeabikerack.views.newrack_form'), 
    (r'^rack/add/$', 'bmabr.buildmeabikerack.views.newrack_add'), 
                       
    (r'^neighborhoods/$', 'bmabr.buildmeabikerack.views.neighborhoods'), 

    (r'^communityboard/$', 'bmabr.buildmeabikerack.views.communityboard'),


#    (r'^@api/rack/$','py.buildmeabikerack.views.api_newrack'), 


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
 #    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),
)
