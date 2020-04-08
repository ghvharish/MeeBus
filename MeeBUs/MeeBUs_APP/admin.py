from django.contrib import admin

# Register your models here.
from .models import PlaceName,DestinationSelect,SourceSelect

admin.site.register(PlaceName)
admin.site.register(DestinationSelect)
admin.site.register(SourceSelect)