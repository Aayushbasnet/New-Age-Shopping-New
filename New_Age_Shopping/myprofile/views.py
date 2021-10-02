from django.shortcuts import render
# Create your views here.
from django.http import request
from django.shortcuts import render, redirect
from account.models import User
from .forms import MyProfileForms
from main_app.models import OrderItem, Comment, Product
from main_app.utils import for_items_total
from .models import MyProfile, ShippingAddress,  ReviewSeller
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# @login_required
def myProfile(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            user_profile = User.objects.get(id = request.user.pk, is_customer = True)
            
            context = {
                'user_profile' : user_profile,
            }
            return render(request, "myprofile/myprofile.html",context)
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')
    else:
        messages.warning(request, "Permission denied! Login with your customer account.")
        return redirect('/account/login/')
    

# @login_required
def updateProfile(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
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
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')
    else:
        messages.warning(request, "Permission denied! Login with your customer account.")
        return redirect('/account/login/')

# @login_required
def shippingAddress1(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            user_profile = User.objects.get(id = request.user.pk, is_customer = True)

            context = {
                'user_profile' : user_profile,
            }
            
            return render(request, "myprofile/shippingaddress.html",context)
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')  
    else:
        messages.warning(request, "Permission denied! Login with your customer account.")
        return redirect('/account/login/')   


def addShippingAddress(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            context = {

            }
            return render(request, "myprofile/AddNewShippingAddress.html",context)
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/') 
    else:
        messages.warning(request, "Permission denied! Login with your customer account.")
        return redirect('/account/login/') 

# @login_required
def myOrder(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            user_profile = User.objects.get(id = request.user.pk, is_customer = True)
            order_items = OrderItem.objects.filter(user = user_profile, complete = True)
            
            print(order_items)
            context={
                'user_profile' : user_profile,
                'order_items' : order_items,
            }
            return render(request, "myprofile/my_order.html",context)
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/') 
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/account/login/')

# @login_required
def myReview(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            user_profile = User.objects.get(id = request.user.pk, is_customer = True)
            my_comment = Comment.objects.filter(user = user_profile)
            print(my_comment)
            context={
                'user_profile' : user_profile,
                'my_comment' : my_comment,
            }

            return render(request, "myprofile/my_review.html",context)
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/account/login/')


def reviewSeller(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            customer_user = User.objects.get(id = request.user.pk, is_customer = True)
            order_items = OrderItem.objects.filter(user = customer_user, received = True)
            rate = ReviewSeller.objects.filter( is_rated = True)
            print("data--------",rate)
            context = {
                'order_items' : order_items,
                'rate' : rate,
            }
            return render(request, 'myprofile/review_seller.html', context)
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')
            
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/account/login/')


def reviewSellerSuccess(request, pk):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            if request.method == "POST" and 'review_btn'+str(pk) in request.POST:
                print("inside post of review seller")
                rate = request.POST.get('rate')
                product = OrderItem.objects.get(pk = pk)
                print(product.product.user)
                review_seller_obj = ReviewSeller.objects.create(
                    user = product.product.user,
                    rate = rate,
                    order_items = product,
                    is_rated = True,
                )
                review_seller_obj.save()
                return redirect('/myprofile/review_seller/')
            else:
                messages.warning(request, "Rating failed")
                return redirect('/myprofile/review_seller/')
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/account/login/')

            