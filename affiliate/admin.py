from django.contrib import admin
from affiliate.models import *
# Register your models here.


class AffiliateFilter(admin.ModelAdmin):
    list_display = ('user', 'aff_name', 'aff_phone', 'aff_email')
    search_fields = ['aff_name']
    list_filter = ('created_at',)


admin.site.register(Affiliate, AffiliateFilter)
