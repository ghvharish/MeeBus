from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is a sample django pro")

def MeeBus(request):
    return render(request,'MeeBus/base.html')

def MeeBusRTC(request):
    return render(request,'MeeBus/rtc.html')

def MeeBusPriv(request):
    return render(request,'MeeBus/private.html')