from django.shortcuts import render
from .forms import *
from django.http import HttpResponse


# Create your views here.
def Signup(request):
    if request.method == "GET":
        data = {"signup_form": SignupForm(), "login_form": LoginForm()}
        return render(request, "signup.html", data)
    else:
        if 'signup' in request.POST:
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("Signup successful")
            else:
                return render(request, "signup.html", {"signup_form": form, "login_form": LoginForm()})

        elif 'login' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                return HttpResponse("Login successful")
            else:
                return render(request, "signup.html", {"login_form": form, "signup_form": SignupForm()})

        else:
            return HttpResponse("Invalid request")
