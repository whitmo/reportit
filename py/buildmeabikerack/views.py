# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import get_object_or_404, render_to_response

from django.contrib.gis.geos import GEOSGeometry, fromstr 

from django.core.mail import send_mail


from py.buildmeabikerack.models import Rack 
from py.buildmeabikerack.models import Neighborhoods
from py.buildmeabikerack.models import RackForm


def index(request):
    if request.method == 'GET':
        recent_request = Rack.objects.all()
        return render_to_response('buildmeabikerack/index.html', {'recent_request': recent_request})
    
    elif request.method == 'POST': 

        return HttpResponse("index, POST")


def newrack(request):         
    if request.method == 'POST': 
        form = RackForm(request.POST)
        form.location = fromstr('POINT(73 43)', srid=4326)
        if form.is_valid(): 
            new_rack = form.save()
            return HttpResponseRedirect('/thanks')
    else: 
        form = RackForm()

    return render_to_response('buildmeabikerack/newrack.html', { 
            'form': form,                   
           })


def rack(request,rack_id): 
    rack_query = Rack.objects.filter(id=rack_id)    
    return render_to_response('buildmeabikerack/rack.html', { 
            'rack_query': rack_query,            
            })


def neighborhoods(request): 
    neighborhood_list = Neighborhoods.objects.all()
    return render_to_response('buildmeabikerack/neighborhoods.html', {'neighborhood_list': neighborhood_list})
