from django.urls import path
from .views import home_page, on_load_oxygen, load_oxygen_cylinder, load_hospital_beds, on_load_beds

urlpatterns = [
    path("", home_page, name="home-page"),
    path("oxygen/", on_load_oxygen, name="oxygen-page"),
    path("oxygen-cylinder-list/", load_oxygen_cylinder, name="oxygen-list"),
    path("hospital-beds-list/", load_hospital_beds, name="hospital-beds"),
    path("beds/", on_load_beds, name="beds-page"),
]