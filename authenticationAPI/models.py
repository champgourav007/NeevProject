from django.db import models
from django.contrib.auth.models import User


class HospitalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=255)
    hospital_address = models.TextField()
    TYPE_CHOICES = (
        ("PRIVATE","PRIVATE"),
        ("GOVERNMENT","GOVERNMENT"),
        ("SEMI-GOVERNMENT","SEMI-GOVERNMENT")
    )
    hospital_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="PRIVATE")
    hospital_code = models.CharField(max_length=100)
    hospital_website = models.CharField(max_length=255)
    
    
class HospitalEmails(models.Model):
    model = models.ForeignKey(HospitalUser, on_delete=models.CASCADE)
    hospital_email = models.EmailField()


class HospitalPhoneNumbers(models.Model):
    model = models.ForeignKey(HospitalUser, on_delete=models.CASCADE)
    phone_number = models.IntegerField()


