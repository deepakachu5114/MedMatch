from django.db import models

class Doctors(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    experience = models.IntegerField()
    contact = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)
    license_number = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    current_medication = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username