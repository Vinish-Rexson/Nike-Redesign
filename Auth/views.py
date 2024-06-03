from django.shortcuts import render
from .forms import *
from django.http import HttpResponse


# Create your views here.
def Signup(request):
    if request.method == "GET":
        data = {"signup_form": SignupForm(), "login_form": LoginForm(), "page": "login"}
        return render(request, "signup.html", data)
    else:
        if 'signup' in request.POST:
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("Signup successful")
            else:
                print(form.errors)
                return render(request, "signup.html", {"signup_form": form, "login_form": LoginForm(), "page": "signup"})

        elif 'login' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                return HttpResponse("Login successful")
            else:
                print(form.errors)
                return render(request, "signup.html", {"login_form": form, "signup_form": SignupForm(), "page": "login"})

        else:
            print(request.POST)
            return HttpResponse("Invalid request")
