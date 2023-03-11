from django.contrib import admin
from affiliate.models import *
# Register your models here.
from import_export import resources


class AffilateResource(resources.ModelResource):
    class Meta:
        models = Affiliate
        fields = ('id', 'status')
        export_order = ('id', 'status')


class AffiliateFilter(admin.ModelAdmin):
    list_display = ('user', 'aff_name', 'aff_phone', 'aff_email')
    search_fields = ['aff_name']
    list_filter = ('created_at',)


admin.site.register(Affiliate, AffiliateFilter)
