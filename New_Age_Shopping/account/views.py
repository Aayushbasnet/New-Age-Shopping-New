from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, LoginUserForm, MerchantForm
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.urls.base import reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView,PasswordResetCompleteView


# from django.contrib.auth.views import LoginView,PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView,PasswordResetCompleteView

def loginPage(request):
    form = LoginUserForm()
    print(form)
    if request.method =="POST":
        form = LoginUserForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_auth = authenticate(username= username, password= password)
            if user_auth is not None:
                login(request, user_auth)
                if request.user.is_authenticated and request.user.is_customer:
                    return redirect('/')
                elif request.user.is_authenticated and request.user.is_merchant:
                    return redirect('/merchant/')
            else:
                messages.warning(request, "Username or password invalid ")
        else:
            messages.warning(request, "Can't Validate")
    else:
        pass
        # messages.warning(request, "There is no item in the cart")
    context ={
        'form' : form,
    }
    return render(request, 'account/login.html', context)

def signupPage(request):
    forms = UserForm()

    # if not request.user.is_authenticated:
    if request.method == "POST":
        print("here!!!!!!")
        forms = UserForm(request.POST)
        if forms.is_valid():
            print("2nda herwe!!!!!!!!!!!!!!!")
            forms.save(commit=False)
            username = forms.cleaned_data.get('username')
            first_name = forms.cleaned_data.get('first_name')
            last_name = forms.cleaned_data.get('last_name')
            email = forms.cleaned_data.get('email')
            password_first = forms.cleaned_data.get('password1')
            print(password_first)
            password_con = forms.cleaned_data.get('password2')
            print(password_con)
            phone_number = forms.cleaned_data.get('phone_number')
            gender = forms.cleaned_data.get('gender')
            address = forms.cleaned_data.get('address')

            merchant_obj = User.objects.create(
                username = username,
                first_name  = first_name,
                last_name = last_name,
                email = email,
                password = make_password(password_first),
                # password2 = password_con,
                phone_number = phone_number,
                gender = gender,
                address = address,

                is_customer = True,
                is_merchant = False,
            )
            print(merchant_obj)

            merchant_obj.save()
            # messages.success(request, "Successfully registered your account !!!")
            return redirect("/account/login/")
    else:
        forms = UserForm()
    # else:
    #     return redirect('/login/')

    
    context = {
        'forms' : forms,
    }
    return render(request, 'account/signup.html', context)

#     # else:
#     #     return redirect('/')

def merchantSignupPage(request):
    forms = MerchantForm()

    # if not request.user.is_authenticated:
    if request.method == "POST":
        print("here!!!!!!")
        forms = MerchantForm(request.POST, request.FILES)
        print(forms)
        if forms.is_valid():
            print("2nda herwe!!!!!!!!!!!!!!!")
            forms.save(commit=False)
            username = forms.cleaned_data.get('username')
            first_name = forms.cleaned_data.get('first_name')
            last_name = forms.cleaned_data.get('last_name')
            email = forms.cleaned_data.get('email')
            password_first = forms.cleaned_data.get('password1')
            print(password_first)
            password_con = forms.cleaned_data.get('password2')
            print(password_con)
            phone_number = forms.cleaned_data.get('phone_number')
            gender = forms.cleaned_data.get('gender')
            address = forms.cleaned_data.get('address')
            pan_number = forms.cleaned_data.get('pan_number')
            document_img = forms.cleaned_data.get('document')

            merchant_obj = User.objects.create(
                username = username,
                first_name  = first_name,
                last_name = last_name,
                email = email,
                password = make_password(password_first),
                # password2 = password_con,
                phone_number = phone_number,
                gender = gender,
                address = address,
                pan_number = pan_number,
                document = document_img,
                is_customer = 'False',
                is_merchant = 'True',
            )

            merchant_obj.save()
            print(merchant_obj)
            # messages.success(request, "Successfully registered your account !!!")
            return redirect("/account/login/")
    else:
        forms = MerchantForm()
    # else:
    #     return redirect('/login/')

    
    context = {
        'forms' : forms,
    }
    return render(request, 'account/merchant_signup.html', context)

def logoutpage(request):
    logout(request)
    return redirect('/account/login/')


class PasswordResetView(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    email_template_name = 'account/password_reset_email.html'
    # success_url = reverse_lazy('password_reset_done')

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'