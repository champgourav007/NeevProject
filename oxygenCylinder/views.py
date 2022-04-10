from django.shortcuts import render
from .models import Cities, State, Hospital


def load_state_cities(clicked_city=None, clicked_state=None):
    states = State.objects.all()
    cities = Cities.objects.all()
    return {
        "states" : states,
        "cities" : cities,
        "clickedstate" : clicked_state,
        "clickedcity" : clicked_city,
        "services" : None,
    }


def home_page(request):
    return render(request, "oxygenCylinder/home_page.html")


def on_load_oxygen(request):
    if request.method == "POST":
        if request.POST.get("state"):
            state = State.objects.get(name=request.POST["state"])
            cities = Cities.objects.filter(state_id=state.pk)
            context = load_state_cities()
            context["cities"] = cities
            context["clickedstate"] = request.POST["state"]
            print(context["clickedstate"])
            return render(request, "oxygenCylinder/oxygen-cylinders.html",context=context)
    context = load_state_cities()
    return render(request, "oxygenCylinder/oxygen-cylinders.html", context=context)



def load_oxygen_cylinder(request):
    if request.method == "POST":
        cityId = request.POST["city"]
        hospitals = Hospital.objects.filter(city_id=cityId)
        context = load_state_cities()
        context["services"] = hospitals
        context["clickedcity"] = Cities.objects.get(pk=cityId)
        print(context["clickedcity"])
        return render(request, "oxygenCylinder/oxygen-cylinders.html", context=context)

    context = load_state_cities()
    return render(request, "oxygenCylinder/oxygen-cylinders.html", context=context)



def on_load_beds(request):
    if request.method == "POST":
        if request.POST.get("state"):
            state = State.objects.get(name=request.POST["state"])
            cities = Cities.objects.filter(state_id=state.pk)
            context = {
                "states" : State.objects.all(),
                "cities" : cities,
                "services" : None,
            }
            return render(request, "oxygenCylinder/hospital-beds.html",context=context)
    context = load_state_cities()
    return render(request, "oxygenCylinder/hospital-beds.html", context=context)



def load_hospital_beds(request):
    if request.method == "POST":
        cityId = request.POST["city"]
        hospitals = Hospital.objects.filter(city_id=cityId)
        context = load_state_cities()
        context["services"] = hospitals
        return render(request, "oxygenCylinder/hospital-beds.html", context=context)

    context = load_state_cities()
    return render(request, "oxygenCylinder/hospital-beds.html", context=context)

