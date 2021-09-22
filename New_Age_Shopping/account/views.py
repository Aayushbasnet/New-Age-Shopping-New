from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.

def loginPage(request):
    context ={}
    return render(request, 'account/login.html', context)

def signupPage(request):
    form    =   CreateUserForm()

    if request.method == 'POST':
        form    =   CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return('login')
        


    context =   {
        'form'  :   form,
    }
    return render(request, 'account/signup.html', context)