from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.template import loader
from django.contrib import messages
from django.http.response import JsonResponse
import json
from .forms import CheckoutForm, CommentForm
from django.core.exceptions import ObjectDoesNotExist
from .utils import for_items_total
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


def homepage(request):
    first_slide_homepage_product_data       =   Product.objects.all().order_by('?')[:7]
    featured_slider_product                 =   FeaturedSliderProduct.objects.all()
    
    context =  {
        "first_slide_homepage_product_data"     :   first_slide_homepage_product_data,  
        "featured_slider_product"                :   featured_slider_product,
    }

    return render(request, 'main_app/homepage.html', context)

def shop_now(request):
    print("running yes")
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'main_app/shop_now.html', context)

def category_shopping(request, slug, pk=1):
    print("inside category shopping")
    query_exists = True if len(request.GET) > 0 else False
    print(request.get_full_path())
    search_key = request.GET.get('search_key')
    sort_key = request.GET.get('sort')
    price_min_key = request.GET.get('price_min')
    price_max_key = request.GET.get('price_max')
    print(sort_key)
    print(search_key)
    if slug != 'search' or search_key is None:
        products = Product.objects.filter(Q(product_category__category_name_level2__category_level2__icontains = slug) | Q(product_category__brand_name__icontains = slug))
        
    else:
        products = Product.objects.filter(Q(product_name__icontains = search_key) | 
                                          Q(product_description__icontains = search_key) |
                                          Q(product_category__brand_name__icontains = search_key) |
                                          Q(product_category__category_name_level2__category_level2__icontains = search_key) |
                                          Q(product_category__category_name_level2__category_name_level1__category_level1__icontains = search_key))
    
    if slug == "merchant":
        print("I am here")
        products = Product.objects.filter(user_id = pk)
       
    
    if sort_key is not None:
        if sort_key=='price_asc':
            products = products.order_by('product_price')
        elif sort_key == "price_desc":
            products = products.order_by('-product_price')
    if price_min_key:
        products = products.filter(product_price__gte = price_min_key)
    if price_max_key:
        products = products.filter(product_price__lte=price_max_key)
    search_key = search_key if search_key else slug if search_key or slug else ''
    context = {
        'products' : products,
        'query_exists': query_exists,
        'search_key':  search_key,
        'current_url' : request.get_full_path(),
        'price_max_key': price_max_key,
        'price_min_key' : price_min_key,
        
    }
    return render(request, 'main_app/shop_now.html', context)

def detail(request, pk):
    singleProduct   =   Product.objects.get(id = pk)
    comments        =   Comment.objects.filter(product__id = pk, status=True)
    # print(id)
    context =   {
        "singleProduct"   :   singleProduct,
        "comments"        :   comments,
    }
    return render(request, 'main_app/detail.html', context)

def cart(request):
    if request.method == "POST":
        detail_item_id = request.POST.get("detail_item_id")
        product = get_object_or_404(Product, pk= detail_item_id)
        data = OrderItem.objects.filter(user = request.user, product = product)
        if data.exists():
            first_data = data[0]
            # first_data.quantity += 1
            # first_data.save()
            messages.success(request, "Item added to cart")
        else:
            data = OrderItem.objects.create(user = request.user, product = product)
            data.save()
            messages.success(request, "Item added to cart")
    cart_items = OrderItem.objects.filter(user = request.user)
    order_items = Order.objects.filter(user = request.user)
    grand_total= 0
    for items in cart_items:
        grand_total = grand_total + float(items.get_total)

    items_total= 0
    for items in cart_items:
        items_total = items_total + 1

        
    context ={
        "cart_items" : cart_items,
        "order_items": order_items,
        "grand_total": grand_total,
        "items_total": items_total,
    }

    return render(request, 'main_app/cart.html', context)

def remove_cart(request):
    if request.method == "POST":
        remove_item_id = request.POST.get("remove_cart_id")
        product = get_object_or_404(OrderItem, pk= remove_item_id)
        product.delete()
        messages.warning(request, "Item deleted from cart")
        return redirect("/cart/")
    return render(request, 'main_app/cart.html')

def whishlist(request):
    return render(request, 'main_app/whishlist.html')

# def update_item(request):
#     return render(request, 'main_app/cart.html')

def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user
    product = get_object_or_404(Product,id= productId)

    order_items = OrderItem.objects.filter(user = request.user, product = product)

    if order_items.exists():
        order_item = order_items[0]
        if action == 'add':
            order_item.quantity = (order_item.quantity + 1)
            order_item.save()
        elif action == 'remove':
            order_item.quantity = (order_item.quantity - 1)
            order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()


    return JsonResponse('Item was added', safe=False)
    

def contact_us(request):
    return render(request, 'main_app/contact_us.html')

def about_us(request):
    return render(request, 'main_app/about_us.html')

@login_required
def checkout(request):
    forms = CheckoutForm()
    if request.method == "POST":
        forms = CheckoutForm(request.POST or None)
        try:
            order =   OrderItem.objects.filter(user = request.user, complete=False)
            if order.exists():
                if forms.is_valid():
                    first_name  = forms.cleaned_data.get("first_name")
                    last_name   =  forms.cleaned_data.get("last_name")
                    email   =  forms.cleaned_data.get("email")
                    phone_number    =   forms.cleaned_data.get("phone_number")
                    shipping_district   =  forms.cleaned_data.get("shipping_district")
                    shipping_address    =   forms.cleaned_data.get("shipping_address")
                    shipping_zip    =   forms.cleaned_data.get("shipping_zip")
                    payment_option  = forms.cleaned_data.get("payment_option")
                    print(forms.cleaned_data)

                    shipping_address    =   ShippingAddress.objects.create(
                        user    =   request.user,
                        first_name  =  first_name, 
                        last_name   =   last_name,
                        email   =   email,
                        phone_number    =   phone_number,
                        shipping_district   =  shipping_district, 
                        shipping_address    =   shipping_address,
                        shipping_zip    =   shipping_zip,
                        payment_option  =   payment_option,
                    )
                    shipping_address.save()
                    return redirect('/payment_view/')
                else:
                    print("form not valid")
            else:
                print("There is no items in cart")
                messages.warning(request, "There is no item in the cart")
        except ObjectDoesNotExist:
            print("No items")
            messages.error(request,"No items found in the cart")
    else:
        forms =CheckoutForm()
    
    context = {
        'forms' : forms,
    }
    return render(request, 'main_app/checkout.html', context)

@login_required
def payment_view(request):
    grand_total, item_total = for_items_total(request)
    ordered_items   =   OrderItem.objects.filter(user = request.user, complete = False)
    context = {
        'ordered_items' : ordered_items,
        'grand_total' : grand_total,
        'item_total' : item_total,
    }
    print(ordered_items)
    return render(request, 'main_app/payment_view.html', context)


def addComment(request, pk):
    url = request.META.get('HTTP_REFERER')+"#pills-review" # get last url
    print(url)
    print("I am inside")
    # return HttpResponse(url)
    if request.method == "POST":
        print("post")
        form = CommentForm(request.POST)
        if form.is_valid():
            print("form valid")
            data = Comment()    # create relation with model
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product = Product.objects.get(pk=pk)
            data.user = request.user
            data.save()
            messages.success(request, "Thank you for your review")
            return HttpResponseRedirect(url)
        else:
            print("not valid")
    else:
        print("POST not valid")

    return HttpResponseRedirect(url)

def totalMerchant(request):
    merchant = User.objects.filter(is_merchant = True)
    product_list = []
    for mer in merchant:
        merchant_total_product = Product.objects.filter(user = mer, user__is_merchant = True).count()
        product_list.append(merchant_total_product)
    print(product_list)
    
    context={
        'merchant_list' : merchant,
        'product_list' : product_list,
    }
    return render(request, 'main_app/merchant_list.html', context)
