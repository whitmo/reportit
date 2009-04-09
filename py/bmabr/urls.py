from django.conf.urls.defaults import *

from bmabr.buildmeabikerack import views 
from django.conf import settings

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    (r'^$', 'bmabr.buildmeabikerack.views.index'), 
    (r'assess/$','bmabr.buildmeabikerack.views.assess'),
    (r'^rack/(?P<rack_id>\d+)/$', 'bmabr.buildmeabikerack.views.rack'),                        
   

     # KML URL 

    (r'rack/all.kml$', 'bmabr.buildmeabikerack.views.rack_all_kml'),
    (r'rack/requested.kml$', 'bmabr.buildmeabikerack.views.rack_requested_kml'),
    (r'rack/pendding.kml$', 'bmabr.buildmeabikerack.views.rack_pendding_kml'),
    (r'rack/built.kml$', 'bmabr.buildmeabikerack.views.rack_pendding_kml'),
    (r'rack/(?P<rack_id>\d+).kml', 'bmabr.buildmeabikerack.views.rack_by_id_kml'),


    # different views for adding infomation, rack, comments. 

    (r'^rack/new/$', 'bmabr.buildmeabikerack.views.newrack_form'), # view for rack request form. 
    (r'^rack/add/$', 'bmabr.buildmeabikerack.views.add_rack'), 
    (r'^comment/add/$', 'bmabr.buildmeabikerack.views.add_comment'), 
                       
    # different ways of viewing information                   

    (r'^neighborhoods/$', 'bmabr.buildmeabikerack.views.neighborhoods'), 
    (r'^communityboard/$', 'bmabr.buildmeabikerack.views.communityboard'),


    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT,'show_indexes': True}),



    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
 #    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),
)
