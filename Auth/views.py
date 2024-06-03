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
            print("POST")
            form = SignupForm(request.POST)
            if form.is_valid():
                print("Valid")
                email = form.cleaned_data['Email']
                password = form.cleaned_data['Password']
                print(email, password)
                form.save()
                return HttpResponse("Signup successful")
            else:
                print(form.errors)
                return render(request, "signup.html", {"signup_form": form, "login_form": LoginForm()})

        elif 'login' in request.POST:
            print("POST LOGIN")
            form = LoginForm(request.POST)
            if form.is_valid():
                print("Valid")
                email = form.cleaned_data['Email']
                password = form.cleaned_data['Password']
                print(email, password)
                return HttpResponse("Login successful")
            else:
                print(form.errors)
                return render(request, "signup.html", {"login_form": form, "signup_form": SignupForm()})

        else:
            print(request.POST)
            return HttpResponse("Invalid request")
