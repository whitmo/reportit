
from bmabr.buildmeabikerack.models import Rack 
from bmabr.buildmeabikerack.models import Neighborhoods
from bmabr.buildmeabikerack.models import CommunityBoard


from django.contrib.gis import admin




class RackAdmin(admin.GeoModelAdmin): 
    list_display = ('address','location')

admin.site.register(Rack, RackAdmin)

class NeighborhoodsAdmin(admin.GeoModelAdmin): 
    list_display = ('name','county')

admin.site.register(Neighborhoods,NeighborhoodsAdmin)


class CommunityBoardAdmin(admin.GeoModelAdmin): 
    list_display = ('name','gid')

admin.site.register(CommunityBoard,CommunityBoardAdmin)
