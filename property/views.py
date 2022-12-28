import socket
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from .forms import *
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from datetime import date


def home(request):
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(local_ip)

    agent_obj = Agent.objects.all().first()
    agent = {
        "aname": agent_obj.name
    }
    # print(agent['name'])
    return render(request, 'index.html', agent)


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('cpassword')

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username Already Taken.')
                return redirect("sign-up")
            if User.objects.filter(email=email).first():
                messages.success(request, 'Email Already Taken.')
                return redirect('sign-up')

            if password == password2:
                user_obj = User.objects.create_user(username, email, password)
                user_obj.save()
                print("user_created")
                auth_token = str(uuid.uuid4())
                profile_obj = Profile(user=user_obj, auth_token=auth_token)
                profile_obj.save()
                send_email_after_registration(email, auth_token)

                return redirect('home')
        except Exception as e:
            print("Daily limit Exceed")
    return render(request, 'sign-up.html')


def send_email_after_registration(email, token):
    subject = "Your accounts need to be verified!!"
    n1 = "\n"
    message = f'Hi click the link to verify your account http://127.0.0.1:8000//verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj.is_verified:
            messages.add_message(request, messages.INFO,
                                 "E-mail is already Verified!")
            return redirect('login')
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            messages.add_message(request, messages.INFO,
                                 "E-mail Verified Successfull")
            return redirect('email-verify')
        else:
            return redirect('error')

    except Exception as e:
        print("EXCEPT")
        print(e)


def email_verify(request):
    return render(request, 'auth/email-verify.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.filter(email=email).first()
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'sign-in.html')


def signout(request):
    logout(request)
    return redirect('home')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_create = Contact(
            name=name, email=email, phone=phone, subject=subject, message=message)
        contact_create.save()

        return redirect(home)

    # fn = ContactForm
    data = {
        # 'form': fn,
    }
    return render(request, 'contact.html', data)


def about(request):
    return render(request, 'about.html')


def profile(request):
    return render(request, 'profile.html')


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


def agency_list(request):
    agency_all = sorted(Agency.objects.all())
    print(agency_all)
    return render(request, 'agency/agency-list.html', {"agency_list": agency_all})


def agency_details(request, agency_name):
    agency_obj = Agency.objects.filter(agency_name=agency_name).first()
    return render(request, 'agency/agency-details.html', {'agency': agency_obj})

# def agency_details(request):
#     return render(request, 'agency-details.html')


def agent_registeration(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            aname = request.POST.get('name')
            agency = request.POST.get('agency')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            description = request.POST.get('description')
            facebook = request.POST.get('facebook')
            instagram = request.POST.get('instagram')
            image = request.FILES['image']

            agent_create = Agent(user=request.user, name=aname, agency=agency, phone=phone, email=email,
                                 description=description, facebook=facebook, instagram=instagram, image=image)
            agent_create.save()
            print("Agent Create")
            return redirect('agent-list')
    else:
        return redirect('sign-in')

    return render(request, 'agent/agent-registeration.html')


def agent_list(request):
    agent_all = Agent.objects.all()
    count = agent_all.count()
    agent_group = []
    for i in agent_all:
        ap = agent_group.append(i)
    # agent_group
    # iterations for 6
    variables = {
        "count": count,
        "agent_list": agent_group
    }
    return render(request, 'agent/agent-list.html', variables)


def agent_details(request, username):
    agent_obj = Agent.objects.filter(user=username).first()
    return render(request, 'agent/agent-details.html', {'agent': agent_obj})


def property_details(request):
    return render(request, 'property/property-details.html')
