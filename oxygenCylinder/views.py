from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, "oxygenCylinder/home_page.html")

def find_oxygen_cylinder(request):
    return render(request, "oxygenCylinder/cylinders.html")