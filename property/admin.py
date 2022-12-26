from django.contrib import admin
from .models import *

# Register your models here.


class ContactFilter(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject')


class AgentDisplay(admin.ModelAdmin):
    list_display = ('user', 'name', "agency", 'email', 'phone', "created_at")


class AgencyDisplay(admin.ModelAdmin):
    list_display = ('user', 'agency_name', 'agency_email', 'agency_phone')


admin.site.register(Contact, ContactFilter)
admin.site.register(Agent, AgentDisplay)
admin.site.register(Agency, AgencyDisplay)
admin.site.register(Profile)
