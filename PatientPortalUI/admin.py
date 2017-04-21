from django.contrib import admin
from .models import PatientRecord, Medication, Visit, Vital, Profile


# Register your models here.
class ProfileDetail(admin.ModelAdmin):
    list_display = ("user", "birth_date", "street_line1", "zipcode", "city", "state")


class MedicationDetail(admin.ModelAdmin):
    list_display = ("medication_name",)


class VitalDetail(admin.ModelAdmin):
    list_display = ("date", "user", "height", "weight", "systolic", "diastolic")


# Register the model we made in models.py with the Django
# admin
admin.site.register(PatientRecord)
admin.site.register(Medication, MedicationDetail)
admin.site.register(Visit)
admin.site.register(Vital, VitalDetail)
admin.site.register(Profile, ProfileDetail)
