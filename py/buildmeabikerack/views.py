# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.gis.geos import *


from py.buildmeabikerack.models import Rack 
from py.buildmeabikerack.models import Neighborhoods


def index(request):
    if request.method == 'GET':
        recent_request = Rack.objects.all()
        return render_to_response('buildmeabikerack/index.html', {'recent_request': recent_request})
    
    elif request.method == 'POST': 
        return HttpResponse("index, POST")

#def adddrack(request): 
 

def newrack(request): 
    return render_to_response('buildmeabikerack/newrack.html')


def neighborhoods(request): 
    neighborhood_list = Neighborhoods.objects.all()
    return render_to_response('buildmeabikerack/neighborhoods.html', {'neighborhood_list': neighborhood_list})
