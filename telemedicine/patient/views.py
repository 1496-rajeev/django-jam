from django.shortcuts import render
from django.http import HttpResponse
from patient.models import Patient
from patient.forms import PatientForm 


# Create your views here.
def index(request):
    return render(request, 'patient/index.html')

def patientView(request):
    patients = Patient.objects.all()
    patientDict = {'patients':patients}
    return render(request, 'patient/index.html', context=patientDict)

def PatientFormView(request):
    form=PatientForm ()
    formDict = {'form':form}
    if request.method=='POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'patient/index.html',context=formDict)
