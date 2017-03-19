from django.contrib import admin
from .models import PatientRecord, Medication, Visit

# Register your models here.

# Register the model we made in models.py with the Django
# admin
admin.site.register(PatientRecord)
admin.site.register(Medication)
admin.site.register(Visit)
