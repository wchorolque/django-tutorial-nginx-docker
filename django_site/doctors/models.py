from django.db import models
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import EmailField
from django.db.models import ForeignKey
from django.db.models import TextField
from django.db.models import TimeField


class Doctor(models.Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    qualification = CharField(max_length=100)
    contact_number = CharField(max_length=20)
    email = EmailField()
    address = TextField()
    biography = TextField()


class Department(models.Model):
    name = CharField(max_length=100)
    description = TextField()


class DoctorAvailability(models.Model):
    doctor = ForeignKey(Doctor, related_name="availabilities", on_delete=models.CASCADE)
    start_date = DateField(max_length=10)
    end_date = DateField(max_length=10)
    start_time = TimeField()
    end_time = TimeField()


class MedicalNote(models.Model):
    doctor = ForeignKey(Doctor, related_name="medical_notes", on_delete=models.CASCADE)
    note = TextField()
    date = DateField()
