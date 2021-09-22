from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class MerchantForm(UserCreationForm):
    class Meta:
        model   =   User
        fields = ['username','first_name','last_name','email', 'password1', 'password2', 'phone_number', 'gender','address', 'pan_number', 'document']

class UserForm(UserCreationForm):
    class Meta:
        model   =   User
        fields = ['username','first_name','last_name','email', 'password1', 'password2', 'phone_number', 'gender','address']



class LoginUserForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class" : "form-control"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class" : "form-control"
            }
        )
    )
