from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=11, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    street_line1 = models.CharField(max_length=100, blank=True)
    street_line2 = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


# Basic model for storing patient records
class PatientRecord(models.Model):
    user = models.OneToOneField(User, default=None)

    def __str__(self):
        return self.user.username


# Basic model for storing medication data
class Medication(models.Model):
    medication_name = models.CharField(max_length=30, blank=True, default=None)
    description = models.TextField(max_length=400, null=True, default='')


class Vital(models.Model):
    date = models.DateField(blank=True, default=date.today)
    user = models.ForeignKey(User, blank=False, default=None)
    height = models.CharField(max_length=200, default="5'7\"")
    temp = models.DecimalField(max_digits=5, decimal_places=1, default=98.7)
    weight = models.DecimalField(max_digits=5, decimal_places=1, default=180)
    systolic = models.DecimalField(max_digits=3, decimal_places=0, default=120)
    diastolic = models.DecimalField(max_digits=3, decimal_places=0, default=80)


# Basic model for storing patient visit data
class Visit(models.Model):
    reason_for_visit = models.TextField(max_length=200)
    date_of_visit = models.DateField(default=None)
    record = models.ForeignKey(PatientRecord, default=None)
