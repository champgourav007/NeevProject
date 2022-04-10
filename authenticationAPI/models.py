from django.db import models
from django.contrib.auth.models import User


# class HospitalUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     hospital_name = models.CharField(max_length=255)
#     hospital_address = models.TextField()

#     TYPE_CHOICES = (
#         ("PRIVATE","PRIVATE"),
#         ("PUBLIC","PUBLIC"),
#     )

#     hospital_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="PRIVATE")
#     hospital_code = models.CharField(max_length=255)
#     hospital_website = models.CharField(max_length=255)
#     contact_details = models.CharField(max_length=255)
#     hospital_state = models.CharField(max_length=100)
#     hospital_city = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.hospital_name}"
    