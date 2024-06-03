from django import forms
from .models import Customer


class SignupForm(forms.Form):
    Name = forms.CharField(max_length=50)
    Email = forms.EmailField(max_length=50)
    Password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    Confirm_Password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def Password_clean(self):
        cleaned_data = super().clean()
        Password = cleaned_data.get("Password")
        Confirm_Password = cleaned_data.get("Confirm_Password")

        if Password != Confirm_Password:
            raise forms.ValidationError("Password and Confirm Password must match")
        return cleaned_data

    def Email_clean(self):
        cleaned_data = super().clean()
        Email = cleaned_data.get("Email")
        if Customer.objects.filter(Email=Email).exists():
            raise forms.ValidationError("Email already exists")
        return cleaned_data

    def Name_clean(self):
        cleaned_data = super().clean()
        Name = cleaned_data.get("Name")
        if Customer.objects.filter(Name=Name).exists():
            raise forms.ValidationError("Name already exists")
        return cleaned_data
