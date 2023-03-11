from django.shortcuts import redirect, render
from affiliate.models import *
from property.models import User, Agent
# Create your views here.


def affiliate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('cname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            affiliate_create = Affiliate(user=request.user, aff_name=name, aff_email=email, aff_phone=phone,
                                         aff_subject=subject, aff_details=message)
            affiliate_create.save()
            return redirect('home')
    else:
        print("User is not Authenticated")
        return redirect('sign-in')
    return render(request, "affiliate/affiliate.html")


def affiliateList(request, pk):
    if request.user.is_authenticated:
        agent = Agent.objects.filter(user_id=pk).first()
        print(agent.user)
        affiliate = reversed(Affiliate.objects.filter(user=agent.user).all())
        print(affiliate)

        content = {
            "affiliates": affiliate,
            "agentName": agent.name,
        }
    else:
        return redirect('sign-in')
    return render(request, 'affiliate/affiliateList.html', content)
