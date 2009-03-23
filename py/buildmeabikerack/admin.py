
from py.buildmeabikerack.models import Rack 
from py.buildmeabikerack.models import Neighborhoods

from django.contrib import admin 

class RackAdmin(admin.ModelAdmin): 
    list_display = ('date','location')

admin.site.register(Rack, RackAdmin)


class NeighborhoodsAdmin(admin.ModelAdmin): 
    list_display = ('name','county')

admin.site.register(Neighborhoods,NeighborhoodsAdmin)
