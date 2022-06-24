from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.HospitalUser)
admin.site.register(models.UserAccount)
admin.site.register(models.UserBookings)
