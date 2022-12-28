from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),

    path('sign-in/', views.signin, name='sign-in'),
    path('sign-up/', views.signup, name='sign-up'),
    path('sign-out/', views.signout, name='sign-out'),

    # Email Verification
    path('email-verification/', views.email_verify, name='email-verify'),
    path('verify/<auth_token>', views.verify, name='verify'),


    path('agency-registeration/', views.agency_registeration,
         name='agency-registeration'),
    path('agency-list/', views.agency_list,
         name='agency-list'),
    path('agency-details/<agency_name>', views.agency_details,
         name='agency-details'),
    # path('agency-details/', views.agency_details,
    #      name='agency-details'),

    path('agent-registeration/', views.agent_registeration,
         name='agent-registeration'),
    path('agent-details/<username>', views.agent_details,
         name='agent-details'),
    path('agent-list/', views.agent_list,
         name='agent-list'),

    path('property-details/', views.property_details,
         name='property-details'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
