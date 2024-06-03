from django import forms
from .models import Customer


class SignupForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Name', 'Email', 'Password']
        include = ['C_Password']
        Name = forms.CharField(max_length=50)
        Email = forms.EmailField(max_length=50)
        Password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    Confirm_Password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_Password(self):
        Password = self.cleaned_data.get("Password")
        if len(Password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        return Password

    def clean_Confirm_Password(self):
        Password = self.cleaned_data.get("Password")
        Confirm_Password = self.cleaned_data.get("Confirm_Password")
        if Password != Confirm_Password:
            raise forms.ValidationError("Password does not match")
        return Confirm_Password

    def clean_Email(self):
        Email = self.cleaned_data.get("Email")
        if Customer.objects.filter(Email=Email).exists():
            raise forms.ValidationError("Email already exists")
        return Email
    def clean_Name(self):
        Name = self.cleaned_data.get("Name")
        if Customer.objects.filter(Name=Name).exists():
            raise forms.ValidationError("Name already exists")
        return Name

class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Email', 'Password']
        Email = forms.EmailField(max_length=50)
        Password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_Email(self):
        Email = self.cleaned_data.get("Email")
        if not Customer.objects.filter(Email=Email).exists():
            raise forms.ValidationError("Email does not exist")
        return Email

    def clean_Password(self):
        Email = self.cleaned_data.get("Email")
        Password = self.cleaned_data.get("Password")
        if not Customer.objects.filter(Email=Email, Password=Password).exists():
            raise forms.ValidationError("Password is incorrect")
        return Password
