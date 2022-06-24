from django.db import models
from django.contrib.auth.models import User
from oxygenCylinder import models as model

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}"

class HospitalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    hospital = models.OneToOneField(model.Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"
    
class UserBookings(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    booking = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user_account}"
