from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import City


class UserLocationAdmin(LeafletGeoAdmin):
    pass
    #list_display = ('name', 'location')

admin.site.register(City,UserLocationAdmin)
