from django.contrib import admin
from .models import *

# Register your models here.


class ContactFilter(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject')


class AgentDisplay(admin.ModelAdmin):
    list_display = ('user', 'name', "agency", 'email', 'phone', "created_at")


class AgencyDisplay(admin.ModelAdmin):
    list_display = ('user', 'agency_name', 'agency_email', 'agency_phone')


class PropertyDisplay(admin.ModelAdmin):
    list_display = ('agency_name', 'title', 'state', 'city', 'property_price')
    search_fields = ['title']
    list_filter = ('state', 'city', 'property_price')


class SchecudeDisplay(admin.ModelAdmin):
    list_display = ('created_at', "name", "agency_name", "phone")
    list_filter = ("created_at",)


class MapDisplay(admin.ModelAdmin):
    list_display = ("location", "created_at")
    list_filter = ("created_at", "location",)
    search_fields = ['location']


admin.site.register(Contact, ContactFilter)
admin.site.register(Agent, AgentDisplay)
admin.site.register(Agency, AgencyDisplay)
admin.site.register(Profile)
admin.site.register(Property, PropertyDisplay)
admin.site.register(ForgotPassword)
admin.site.register(Schedule, SchecudeDisplay)
admin.site.register(MapLocater, MapDisplay)
