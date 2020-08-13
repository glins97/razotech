from django.contrib import admin
from .models import *

class LampAdmin(admin.ModelAdmin):
    list_display = ('space', 'description', 'status', 'mac')

class AirConditioningAdmin(admin.ModelAdmin):
    list_display = ('space', 'description', 'status', 'temperature', 'mac')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('person', 'device', 'status')

admin.site.register(Lamp, LampAdmin)
admin.site.register(AirConditioning, AirConditioningAdmin)

admin.site.register(Mobile)
admin.site.register(Web)
admin.site.register(Request, RequestAdmin)
admin.site.register(Access)

admin.site.register(Building)
admin.site.register(Space)
admin.site.register(Person)
