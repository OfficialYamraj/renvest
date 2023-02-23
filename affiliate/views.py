from django.shortcuts import render

# Create your views here.


def affiliate(request):
    return render(request, "affiliate/affiliate.html")
