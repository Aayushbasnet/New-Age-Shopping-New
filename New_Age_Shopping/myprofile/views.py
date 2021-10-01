from django.shortcuts import render

# Create your views here.
from django.http import request
from django.shortcuts import render, redirect
from account.models import User
from .forms import MyProfileForms
from main_app.models import OrderItem, Comment
from main_app.utils import for_items_total
from .models import MyProfile, ShippingAddress
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def myProfile(request):
    if request.user.is_customer or request.user.is_superuser:
        user_profile = User.objects.get(id = request.user.pk, is_customer = True)
        
        context = {
            'user_profile' : user_profile,
        }
        return render(request, "myprofile/myprofile.html",context)
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/')
    

@login_required
def updateProfile(request):
    update_form = MyProfileForms(instance=request.user)
    print (update_form)
    if request.method == "POST":
        update_form = MyProfileForms( request.POST,instance=request.user)

        print("-----------I am update profile")
        if update_form.is_valid():
            print("-------------I am valid")
            update_form.save()
            return redirect('/myprofile/')
        else:
            print("Invalid ")
            print (update_form)
    context = {
        'update_form' : update_form,
    }
    if request.user.is_customer or request.user.is_superuser:
        return render(request, "myprofile/update_profile.html",context)
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/')

@login_required
def shippingAddress1(request):
    user_profile = User.objects.get(id = request.user.pk, is_customer = True)
    # address = MyProfile.objects.filter(user = user_profile)
    context = {
        'user_profile' : user_profile,
    }
    if request.user.is_customer:
        return render(request, "myprofile/shippingaddress.html",context)
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/')   

def addShippingAddress(request):
    context = {

    }
    if request.user.is_customer or request.user.is_superuser:
        return render(request, "myprofile/AddNewShippingAddress.html",context)
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/') 

@login_required
def myOrder(request):
    user_profile = User.objects.get(id = request.user.pk, is_customer = True)
    order_items = OrderItem.objects.filter(user = user_profile, complete = True)
    
    print(order_items)
    context={
        'user_profile' : user_profile,
        'order_items' : order_items,
    }
    if request.user.is_customer or request.user.is_superuser:
        return render(request, "myprofile/my_order.html",context)
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/')

@login_required
def myReview(request):
    user_profile = User.objects.get(id = request.user.pk, is_customer = True)
    my_comment = Comment.objects.filter(user = user_profile)
    print(my_comment)
    context={
        'user_profile' : user_profile,
        'my_comment' : my_comment,
    }
    if request.user.is_customer or request.user.is_superuser:
        return render(request, "myprofile/my_review.html",context)
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/')