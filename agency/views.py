from django.shortcuts import render
from property.views import *

# Create your views here.


def agency_registeration(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            agency_name = request.POST.get('agency_name')
            agency_tagline = request.POST.get('agency_tagline')
            agency_phone = request.POST.get('agency_phone')
            agency_email = request.POST.get('agency_email')
            agency_description = request.POST.get('agency_description')
            agency_facebook = request.POST.get('agency_facebook')
            agency_instagram = request.POST.get('agency_instagram')
            agency_image = request.FILES['agency_image']

            agency_create = Agency(user=request.user, agency_name=agency_name,
                                   agency_tagline=agency_tagline, agency_phone=agency_phone, agency_email=agency_email,
                                   agency_description=agency_description, agency_facebook=agency_facebook,
                                   agency_instagram=agency_instagram, agency_image=agency_image)
            agency_create.save()

            return redirect('home')
    else:
        return redirect('sign-in')

    return render(request, 'agency/agency-registeration.html')


def agency_updatation(request, pk):
    agencyDetails = 20
    pass


def agency_list(request):
    agency_all = sorted(Agency.objects.all())
    print(agency_all)
    return render(request, 'agency/agency-list.html', {"agency_list": agency_all})





def agency_details(request, agency_name):
    agency_obj = Agency.objects.filter(agency_name=agency_name).first()
    ip = get_ip()
    if ip  not in agency_obj.views:
        pass
    return render(request, 'agency/agency-details.html', {'agency': agency_obj})
