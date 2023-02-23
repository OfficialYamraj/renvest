import os
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from property.views import *

# CRUD Of Agents


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


def agent_updatation(request, pk):
    if request.user:
        agentDetail = Agent.objects.filter(id=pk).first()
        if request.method == "POST":
            aname = request.POST.get('name')
            agency = request.POST.get('agency')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            description = request.POST.get('description')
            facebook = request.POST.get('facebook')
            instagram = request.POST.get('instagram')
            image = request.FILES['image']

            if image:
                os.remove(agentDetail.image.path)
            else:
                image = agentDetail.image

            created_at = agentDetail.created_at

            agent_create = Agent(id=pk, user=request.user, name=aname, agency=agency, phone=phone, email=email,
                                 description=description, facebook=facebook, instagram=instagram, image=image, created_at=created_at)
            agent_create.save()
            print("UserUpdate")
            return redirect('agent-details', agentDetail.user.id)

        elif request.user.id == agentDetail.user.id:
            name = agentDetail.name
            print(name)
            agentInfo = {
                "name": name,
                "aname": agentDetail.agency,
                "phone": agentDetail.phone,
                "email": agentDetail.email,
                "description": agentDetail.description,
                "facebook": agentDetail.facebook,
                "instagram": agentDetail.instagram,
            }
            return render(request, "agent/agent-updatation.html", agentInfo)

    # print(agentInfo.values)
    return render(request, "agent/agent-updatation.html", agentInfo)


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
    if request.user.is_authenticated:
        agentDetail = Agent.objects.filter(user=request.user).first()
        # print(request.user.id)
        if request.user.id == agentDetail.user.id:
            edit = True
    else:
        edit = False
    values = {
        "edit": edit,
        'agent': agent_obj
    }
    return render(request, 'agent/agent-details.html', values)
