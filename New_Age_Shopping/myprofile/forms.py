from account.models import User
from django import forms

class MyProfileForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','phone_number', 'address', 'gender')

