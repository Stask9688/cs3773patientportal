from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Basic model for storing patient records
class PatientRecord(models.Model):
    user = models.OneToOneField(User, default=None)


# Basic model for storing medication data
class Medication(models.Model):
    medication_name = models.CharField(max_length=200, default="Ibuprofen")
    record = models.ForeignKey(PatientRecord, default=None)


# Basic model for storing patient visit data
class Visit(models.Model):
    reason_for_visit = models.TextField(max_length=200)
    date_of_visit = models.DateField(default=None)
    record = models.ForeignKey(PatientRecord, default=None)
