from django.contrib import admin
from .models import State, Cities, Hospital, Services
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Hospital)
def createHospitalServices(signal, instance, **kwargs):
    services = Services(hospital=instance)
    services.save()

class ServicesAdmin(admin.ModelAdmin):
    model = Services
    list_display = ['hospital','total_oxygen_cylinders', 'available_oxygen_cylinders', 'total_beds', 'available_beds']
    list_editable = ["total_oxygen_cylinders","available_oxygen_cylinders","total_beds","available_beds"]


admin.site.register(State)
admin.site.register(Cities)
admin.site.register(Hospital)
admin.site.register(Services, ServicesAdmin)