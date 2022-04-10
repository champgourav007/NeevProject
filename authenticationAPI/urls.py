from django.urls import path
from .views import hospitalAPIView
urlpatterns = [
    path("", hospitalAPIView, name="hospital-api-view"),
]
