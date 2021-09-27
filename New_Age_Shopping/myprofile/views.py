from django.shortcuts import render

# Create your views here.
from django.http import request
from django.shortcuts import render, redirect
from account.models import User
from .forms import MyProfileForms
from main_app.models import OrderItem, Comment
from main_app.utils import for_items_total
from .models import MyProfile, ShippingAddress
# Create your views here.

def myProfile(request):
    user_profile = User.objects.get(id = request.user.pk, is_customer = True)
    
    context = {
        'user_profile' : user_profile,
    }
    return render(request, "myprofile/myprofile.html",context)

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

    return render(request, "myprofile/update_profile.html",context)

def shippingAddress1(request):
    # user_profile = User.objects.get(id = request.user.pk, is_customer = True)
    # address = MyProfile.objects.filter(user = user_profile)
    context = {
        # 'address' : address,s
    }
    return render(request, "myprofile/shippingaddress.html",context)

def addShippingAddress(request):
    context = {

    }
    return render(request, "myprofile/AddNewShippingAddress.html",context)

def myOrder(request):
    user_profile = User.objects.get(id = request.user.pk, is_customer = True)
    order_items = OrderItem.objects.filter(user = user_profile, complete = True)
    
    print(order_items)
    context={
        'user_profile' : user_profile,
        'order_items' : order_items,
    }
    return render(request, "myprofile/my_order.html",context)

def myReview(request):
    user_profile = User.objects.get(id = request.user.pk, is_customer = True)
    my_comment = Comment.objects.filter(user = user_profile)
    print(my_comment)
    context={
        'my_comment' : my_comment,
    }
    return render(request, "myprofile/my_review.html",context)