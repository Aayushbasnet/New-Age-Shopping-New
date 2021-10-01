from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class MerchantForm(UserCreationForm):
    class Meta:
        model   =   User
        fields = ['username','first_name','last_name','email', 'password1', 'password2', 'shop_name', 'phone_number', 'gender','address', 'pan_number', 'document']

    def clean_pan_number(self):
        pan_number = self.cleaned_data['pan_number']
        if len(str(pan_number)) != 9:
            raise ValidationError("Pan number must be 9 digits")
        
        return pan_number

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
