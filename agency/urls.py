from django.urls import path
from agency import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('agency-registeration/', views.agency_registeration,
         name='agency-registeration'),
    path('agency-list/', views.agency_list,
         name='agency-list'),
    path('agency-details/<agency_name>', views.agency_details,
         name='agency-details'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
