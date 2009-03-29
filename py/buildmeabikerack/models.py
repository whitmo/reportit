from django.contrib.gis.db import models
from django.forms import ModelForm


# Create your models here.


class Rack(models.Model): 
    location = models.PointField(srid=4326)
    date = models.DateTimeField()    
    address = models.CharField(max_length=200)
    meta = models.TextField()
    contact_email = models.EmailField()
    STATUS_STATE  = ( 
        ('r', 'requested'),
        ('a', 'undering assessment'),
        ('b','built'),
        ('n','not built')
                      
    )
    status = models.CharField(max_length=1, choices=STATUS_STATE)
    objects = models.GeoManager()


'''
class Neighborhoods(models.Model):
    gid = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=43)
    city = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    regionid = models.DecimalField(max_digits=65535, decimal_places=65535)
    the_geom = models.MultiPolygonField() 
    objects = models.GeoManager()

    class Meta:
        db_table = u'gis_neighborhoods'

'''

class RackForm(ModelForm): 
    class Meta: 
        model = Rack 
