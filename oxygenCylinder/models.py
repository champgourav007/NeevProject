from django.db import models


class State(models.Model):
    name = models.CharField(max_length=255, null=False, blank = False)

    def __str__(self):
        return f"{self.name}"

class Cities(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"{self.name}"

class Hospital(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name="hospitals")
    phone_number = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=False, blank=False)
    def __str__(self):
        return f"{self.name}"

class Services(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, primary_key=True,related_name="services")
    total_oxygen_cylinders = models.IntegerField(default=0)
    available_oxygen_cylinders = models.IntegerField(default=0)
    total_beds = models.IntegerField(default=0)
    available_beds = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
