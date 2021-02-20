from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>Eureka Worked!!!<h1/>")

def displaydateTime(request):
    dt=datetime.datetime.now()
    s="<b>current date time is: </b>"+str(dt)
    return HttpResponse(s)

def renderTemplate(request):
    Dict = {"name":"rajeev"}
    return render(request, 'patient/index.html',context=Dict)