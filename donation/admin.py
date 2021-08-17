from django.contrib import admin
# Since the Shop model includes a GeoDjango field, you need to use the special OSMGeoAdmin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import NeedPlasma,DonatePlasma


"""decorated class is a representation of the Shop model in the admin interface and allows customizing different aspects such as the Shop fields that you want to display. In your case, it’s the name and location."""
@admin.register(NeedPlasma)
class NeedAdmin(OSMGeoAdmin):
    list_display = ('name', 'location','person_mobileNumber')

@admin.register(DonatePlasma)
class DonateAdmin(OSMGeoAdmin):
    list_display = ('name', 'location','person_mobileNumber')    