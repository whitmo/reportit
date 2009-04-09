#from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class Issue(models.Model):
    report = models.CharField(max_length=200) 
    date = models.CharField(max_length=30) 
    the_geom = models.PointField(srid=4326)
    objects = models.GeoManager()


