from django.shortcuts import render


# Create your views here.
def hospitalAPIView(request):
    return render(request, "authenticationAPI/signup.html")

