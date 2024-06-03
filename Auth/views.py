from django.shortcuts import render
from .forms import SignupForm

# Create your views here.
def Signup(request):
    if request.method == "GET":
        data = {"form": SignupForm()}
        return render(request, "signup.html", data)