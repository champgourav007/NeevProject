from django.urls import path
from .views import home_page, find_oxygen_cylinder

urlpatterns = [
    path("", home_page, name="home_page"),
    path("find/oxygen/", find_oxygen_cylinder ,name="find-oxygen")
]
