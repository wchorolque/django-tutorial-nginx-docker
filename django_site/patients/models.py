from django.db import models
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import EmailField
from django.db.models import ForeignKey
from django.db.models import TextField


class Patient(models.Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    date_of_birth = DateField()
    contact_number = CharField(max_length=20)
    email = EmailField()
    adress = TextField()
    medical_history = TextField()


class Insurance(models.Model):
    patient = ForeignKey(Patient, related_name="insurances", on_delete=models.CASCADE)
    provider = CharField(max_length=100)
    policy_number = CharField(max_length=100)
    expiration_date = DateField()


class MedicalRecord(models.Model):
    patient = ForeignKey(
        Patient, related_name="medical_records", on_delete=models.CASCADE
    )
    date = DateField()
    diagnosis = TextField()
    treatment = TextField()
    follow_up_date = TextField()

    # doctor = CharField(max_length=100)
    # prescription = TextField()
    # notes = TextField()
