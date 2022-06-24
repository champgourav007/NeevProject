from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def accountView(request):
    return render(request, "authentication/account.html")

def signupView(request):
    if request.method == "POST":
        try:
            data = request.POST
            name = data.get("full_name")
            email = data.get("email")
            password = data.get("password")
        except:
            messages.error(request,"Please enter valid inputs")
            return redirect("account")

        name = name.split(" ")
        last_name = name[-1]
        first_name = " ".join(i for i in name[:len(name)-1])

        user = User.objects.create_user(first_name=first_name,last_name=last_name ,username=email, email=email, password=password)
        user.save()
        messages.success(request, "Account is created Successfully!!!!")

        return redirect("account")

def loginView(request):
    if request.method == "POST":
        try:
            data = request.POST
            email = data.get("email")
            password =data.get("password")
        except:
            messages.error(request, "Please Enter valid inputs")
            return redirect("account")
        try:
            user = auth.authenticate(username=email, password=password)
        except:
            messages.error(request, "Account not found")
            return redirect("account")
        if user is None:
            messages.error(request, "Account not found!!!!")
            return redirect("account")
        else:
            messages.success(request, "Login")
            return redirect("account")
        