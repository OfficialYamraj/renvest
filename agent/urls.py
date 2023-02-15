from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('agent-registeration/', views.agent_registeration,
         name='agent-registeration'),
    path('agent-details/<username>', views.agent_details,
         name='agent-details'),
    path('agent-list/', views.agent_list,
         name='agent-list'),
    path('agent-updatation/<pk>', views.agent_updatation,
         name='agent-updatation'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
