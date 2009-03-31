# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.gis.geos import *


from webmaps.trackit.models import Issue

def index(request):
    if request.method == 'GET':
        return render_to_response('trackit/index.html')    

    elif request.method == 'POST':
        report_form = request.POST['report']
        date_form = request.POST['date'] 
        lat_form = request.POST['lat'] 
        lng_form = request.POST['lng'] 
        point = fromstr('POINT( %s %s)' % (lng_form, lat_form), srid=4326)        
        issue_post = Issue(report=report_form,date=date_form,the_geom=point)
        issue_post.save()
        return HttpResponse("good" )


def map(request): 
    if request.method == 'GET': 
        return  render_to_response('trackit/map.html')
    elif request.method == 'POST': 
        return render_to_response('trackit/error.html')
