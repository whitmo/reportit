
from webmaps.trackit.models import Issue 
from django.contrib import admin 

class IssueAdmin(admin.ModelAdmin): 
    list_display = ('date','the_geom')

admin.site.register(Issue, IssueAdmin)

