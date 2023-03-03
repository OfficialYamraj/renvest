from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.affiliate, name='affiliate'),
    path('List/<int:pk>', views.affiliateList, name='affiliate-list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
