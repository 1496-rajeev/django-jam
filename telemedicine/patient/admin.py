from django.contrib import admin
from patient.models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=['firstName', 'lastName', 'mobile', 'age']

admin.site.register(Patient,PatientAdmin)
