# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import get_object_or_404, render_to_response

from django.contrib.gis.geos import GEOSGeometry, fromstr 
from django.contrib.gis.shortcuts import render_to_kml

from py.buildmeabikerack.models import Rack 
from py.buildmeabikerack.models import RackForm

from geopy import geocoders

def index(request):
    if request.method == 'GET':
        recent_request = Rack.objects.all()
        return render_to_response('buildmeabikerack/index.html', {'recent_request': recent_request})    
    elif request.method == 'POST': 
        return HttpResponse("index,post request")


def newrack_form(request):         
    address = request.GET['address']
    g = geocoders.Google()
    place, (lat, lng) = g.geocode(address)        
    form = RackForm()
    return render_to_response('buildmeabikerack/newrack.html', { 
            'form': form,
            'address': place, 
            'lat': lat,
            'lng': lng,
           })



def newrack_add(request): 
    form = RackForm(request.POST)
    if form.is_valid(): 
        new_rack = form.save()
        return HttpResponseRedirect('/') 
    else: 
        return HttpResponseRedirect('/error/ ') 

def rack(request,rack_id): 
    rack_query = Rack.objects.filter(id=rack_id)    
    return render_to_response('buildmeabikerack/rack.html', { 
            'rack_query': rack_query,            
            })

def rack_all_kml(requst): 
    racks = Rack.objects.all()
    return render_to_kml("placemarkers.kml", {'racks' : racks}) 

def rack_by_kml_id(request, rack_id): 
    racks = Rack.objects.filter(id=rack_id)
    return render_to_kml("placemarkers.kml",{'racks':racks})


'''
def neighborhoods(request): 
    neighborhood_list = Neighborhoods.objects.all()
    return render_to_response('buildmeabikerack/neighborhoods.html', {'neighborhood_list': neighborhood_list})
'''
