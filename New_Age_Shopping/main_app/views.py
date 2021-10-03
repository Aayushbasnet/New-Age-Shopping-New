from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.template import loader
from django.contrib import messages
from django.http.response import JsonResponse
import json
from .forms import CheckoutForm, CommentForm, ContactUsForm
from django.core.exceptions import ObjectDoesNotExist
from .utils import for_items_total, esewa_id
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator



def homepage(request):
    try:
        first_slide_homepage_product_data = Product.objects.all().order_by('?').distinct()[:10]
        trending_product = Product.objects.all().order_by('?')
        our_product = Product.objects.all().order_by('?').distinct()[:22]
        featured_slider_product = FeaturedSliderProduct.objects.all()
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist

    context = {
        "first_slide_homepage_product_data":   first_slide_homepage_product_data,
        "featured_slider_product":   featured_slider_product,
        'trending_product' : trending_product,
        'our_product' : our_product,
    }

    return render(request, 'main_app/homepage.html', context)


def shop_now(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'main_app/shop_now.html', context)


def category_shopping(request, slug, pk=1):

    query_exists = True if len(request.GET) > 0 else False

    search_key = request.GET.get('search_key')
    sort_key = request.GET.get('sort')
    price_min_key = request.GET.get('price_min')
    price_max_key = request.GET.get('price_max')
    min_rating = request.GET.get('min_rating')
    page = request.GET.get('page')

    if slug != 'search' or search_key is None:
        products = Product.objects.filter(Q(product_category__category_name_level2__category_level2__icontains=slug) | Q(
            product_category__brand_name__icontains=slug))

    else:
        products = Product.objects.filter(Q(product_name__icontains=search_key) |
                                          Q(product_description__icontains=search_key) |
                                          Q(product_category__brand_name__icontains=search_key) |
                                          Q(product_category__category_name_level2__category_level2__icontains=search_key) |
                                          Q(product_category__category_name_level2__category_name_level1__category_level1__icontains=search_key))

    if slug == "all":
        products = Product.objects.all()

    if slug == "merchant":
        products = Product.objects.filter(user_id=pk)

    if sort_key is not None:
        if sort_key == 'price_asc':
            products = products.order_by('product_price')
        elif sort_key == "price_desc":
            products = products.order_by('-product_price')

    if price_min_key:
        products = products.filter(product_price__gte=price_min_key)

    if price_max_key:
        products = products.filter(product_price__lte=price_max_key)

    search_key = search_key if search_key else slug if search_key or slug else ''

    if min_rating:
        products = products.annotate(rating_avg = Avg('product_comment__rate'))
        products = products.filter(rating_avg__gte = min_rating)

    paginator = Paginator(products, 35)

    page = page if page else 1

    page_products = paginator.page(page)
    

    context = {
        'products': page_products.object_list,
        'total_pages': paginator.page_range,
        'query_exists': query_exists,
        'search_key':  search_key,
        'current_url': request.get_full_path(),
        'price_max_key': price_max_key,
        'price_min_key': price_min_key,

    }
    return render(request, 'main_app/shop_now.html', context)


def detail(request, pk):
    singleProduct = Product.objects.get(id=pk)
    comments = Comment.objects.filter(product__id=pk, status=True)
    recommend_product = Product.objects.all().order_by('?').distinct()[:5]
    forms = CommentForm()
    context = {
        "singleProduct":   singleProduct,
        "comments":   comments,
        'recommend_product' :recommend_product,
        'forms' : forms
    }
    return render(request, 'main_app/detail.html', context)

# @login_required
def cart(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            if request.method == "POST":
                detail_item_id = request.POST.get("detail_item_id")
                product = get_object_or_404(Product, pk=detail_item_id)
                data = OrderItem.objects.filter(
                    user=request.user, product=product, complete=False)

                if data.exists():
                    first_data = data[0]
                    # first_data.quantity += 1
                    # first_data.save()
                    messages.success(request, "Item added to cart")
                else:
                    data = OrderItem.objects.create(
                        user=request.user, product=product, complete=False)
                    data.save()
                    messages.success(request, "Item added to cart")

            # session products
            cart_items = OrderItem.objects.filter(user=request.user, complete=False)
            order_items = Order.objects.filter(user=request.user,  complete=False)
            grand_total = 0
            for items in cart_items:
                grand_total = grand_total + float(items.get_total)

            items_total = 0
            for items in cart_items:
                items_total = items_total + 1

            usd_total = grand_total * 0.0085

            context = {
                "cart_items": cart_items,
                "order_items": order_items,
                "grand_total": grand_total,
                "items_total": items_total,
                'usd_total': usd_total,
            }
            
            return render(request, 'main_app/cart.html', context)

        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')

    else:
        messages.warning(request, "Permission denied! Login with your customer account.")
        return redirect('/account/login/')

# @login_required
def remove_cart(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            if request.method == "POST":
                remove_item_id = request.POST.get("remove_cart_id")
                product = get_object_or_404(OrderItem, pk=remove_item_id)
                product.delete()
                messages.warning(request, "Item deleted from cart")
                return redirect('/cart/')
                # return render(request, 'main_app/cart.html')
            else:
                messages.warning(request, "Item not removed!")
                return redirect('/cart/')
        
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')

    else:
        messages.warning(request, "Permission denied! Login with your customer account.")
        return redirect('/account/login/')


# navbar wishlist without pk
def nav_wishlist(request):
    products = None
    cart = request.session.get("product_cart")
    if cart is not None:
        i = []
        for p_count in cart:
            i.append(cart[p_count])

        products = Product.objects.filter(pk__in=i)

    context = {
        'products': products,
    }
    return render(request, 'main_app/wishlist.html', context)



# session
def wishlist(request, pk):
    if request.user.is_authenticated:
        if request.user.is_customer:
            messages.warning(request, "Permission denied! You must log out....")
            return redirect('/')
        elif request.user.is_merchant:
            messages.success(request, "Item added.")
            cart = request.session.get("product_cart", None)
            products = None
            if cart is None:
                cart = {}
                request.session["product_cart"] = cart

            cart[pk] = pk

            request.session["product_cart"] = cart
            i = []
            for p_count in cart:
                i.append(cart[p_count])

            products = Product.objects.filter(pk__in=i)

            context = {
                'products': products,
            }
            return render(request, 'main_app/wishlist.html', context)
        else:
            messages.warning(request, "Permission denied! You must log out.")
            return redirect('/')
    else:
        cart = request.session.get("product_cart", None)
        products = None
        if cart is None:
            cart = {}
            request.session["product_cart"] = cart

        cart[pk] = pk

        request.session["product_cart"] = cart
        i = []
        for p_count in cart:
            i.append(cart[p_count])

        products = Product.objects.filter(pk__in=i)

        context = {
            'products': products,
        }
        return render(request, 'main_app/wishlist.html', context)


def remove_wishlist(request, pk):
    try:
        cart = request.session.get("product_cart")
        cart.pop(str(pk))
        request.session["product_cart"] = cart
        return redirect('/wishlist/')
    except:
        return render(request, 'main_app/404.html')



# def wishlist_to_cart(request):
#     return redirect('/account/login/')


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = get_object_or_404(Product, id=productId)

    order_items = OrderItem.objects.filter(user=request.user, product=product)

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
    forms = ContactUsForm()
    if request.method == "POST":
        print("Inside post of contact us")
        forms = ContactUsForm(request.POST or None)
        
        if forms.is_valid():
            forms.save()
            messages.success(request, "Message submitted")
        else:
            messages.success(request, "Message not submitted")


    context = {
        'forms' : forms
    }
    return render(request, 'main_app/contact_us.html', context)


def about_us(request):
    return render(request, 'main_app/about_us.html')


# @login_required
def checkout(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            forms = CheckoutForm()
            if request.method == "POST":
                forms = CheckoutForm(request.POST or None)
                try:
                    order = OrderItem.objects.filter(user=request.user, complete=False)
                    if order.exists():
                        if forms.is_valid():
                            first_name = forms.cleaned_data.get("first_name")
                            last_name = forms.cleaned_data.get("last_name")
                            email = forms.cleaned_data.get("email")
                            phone_number = forms.cleaned_data.get("phone_number")
                            shipping_district = forms.cleaned_data.get(
                                "shipping_district")
                            shipping_address = forms.cleaned_data.get(
                                "shipping_address")
                            shipping_zip = forms.cleaned_data.get("shipping_zip")
                            payment_option = forms.cleaned_data.get("payment_option")

                            shipping_address = ShippingAddress.objects.create(
                                user=request.user,
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                phone_number=phone_number,
                                shipping_district=shipping_district,
                                shipping_address=shipping_address,
                                shipping_zip=shipping_zip,
                                payment_option=payment_option,
                            )
                            shipping_address.save()
                            return redirect('/payment_view/')
                        else:
                            messages.warning(request, "Fill the form correctly!")
                    else:
                        messages.warning(request, "There is no item in the cart")
                except ObjectDoesNotExist:
                    messages.error(request, "No items found in the cart")
            else:
                # forms = CheckoutForm()
                messages.warning(request, "Fill the form correctly!")

            context = {
                'forms': forms,
            }
            
            return render(request, 'main_app/checkout.html', context)
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')
    
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/account/login/')


# @login_required
def payment_view(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            grand_total, item_total = for_items_total(request)
            ordered_items = OrderItem.objects.filter(user=request.user, complete=False)
            code = esewa_id()
            context = {
                'ordered_items': ordered_items,
                'grand_total': grand_total,
                'item_total': item_total,
                'code' : esewa_id,
            }
            return render(request, 'main_app/payment_view.html', context)

        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')

    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/account/login/')


def addComment(request, pk):
    url = request.META.get('HTTP_REFERER')+"#pills-review"  # get last url
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
            pass
    else:
        pass

    return HttpResponseRedirect(url)


def totalMerchant(request):
    merchant = User.objects.filter(is_merchant=True)
    context = {
        'merchant_list': merchant,
        # 'product_list': product_list,
    }
    return render(request, 'main_app/merchant_list.html', context)

# @login_required
def postPayment(request):
    if request.user.is_authenticated:
        if request.user.is_customer or request.user.is_superuser:
            if request.method == "POST":
                data = json.loads(request.body)
                transcation_id = data['transcation_id']
                amount = data['amount']

                payment = Payment.objects.create(stripe_charge_id=transcation_id, user=request.user, amount=amount)
                payment.save()
                
                order_transcation = Order.objects.create(user = request.user, complete =True, transcation_id = request.user.id)
                order_transcation.save()

            ordered_items = OrderItem.objects.filter(user=request.user, complete=False)

            get_shipping_address = ShippingAddress.objects.filter(user=request.user)

            if get_shipping_address.exists():
                get_shipping_address = get_shipping_address[0]
            else:
                return redirect("/checkout/")
            payment_update = Payment.objects.filter(user=request.user)

            if payment_update.exists():
                payment_update = payment_update[0]

            else:
                return redirect("/payment_view/")

            order_transcation =Order.objects.filter(user =request.user)
            if order_transcation.exists():
                order_transcation = order_transcation[0]
                
            if ordered_items.exists():
                ordered_items.update(shipping_address=get_shipping_address)
                ordered_items.update(payment=payment_update)
                ordered_items.update(order=order_transcation)
                ordered_items.update(complete=True)
                
                for items in ordered_items:
                    items.save()
                return redirect('/')

            context = {
                'ordered_items': ordered_items,
            }
            return redirect('/payment_view/')
        
        else:
            messages.warning(request, "Permission denied! Login through your customer account.")
            return redirect('/')
    
    else:
        messages.warning(request, "Permission denied! Login through your customer account.")
        return redirect('/account/login/')

def esewaSuccessful(request):
    oid = request.GET.get('oid')
    amount = request.GET.get('amt')
    refid = request.GET.get('refId')
    

    payment = Payment.objects.create(
        stripe_charge_id = oid,
        user = request.user,
        amount = amount
    )

    payment.save()

    order_transcation = Order.objects.create(user = request.user, complete =True, transcation_id = request.user.id)
    order_transcation.save()

    ordered_items = OrderItem.objects.filter(user=request.user, complete=False)

    get_shipping_address = ShippingAddress.objects.filter(user=request.user)

    if get_shipping_address.exists():
        get_shipping_address = get_shipping_address[0]
    else:
        return redirect("/checkout/")

    payment_update = Payment.objects.filter(user=request.user)
    if payment_update.exists():
        payment_update = payment_update[0]
    else:
        return redirect("/payment_view/")

    order_transcation = Order.objects.filter(user =request.user)
    if order_transcation.exists():
        order_transcation = order_transcation[0]
        
    if ordered_items.exists():
        ordered_items.update(shipping_address=get_shipping_address)
        ordered_items.update(payment=payment_update)
        ordered_items.update(order=order_transcation)
        ordered_items.update(complete=True)
        
        for items in ordered_items:
            items.save()
        messages.warning(request, "Your order is placed")
        return redirect('/')
    messages.warning(request, "Your order is placed")
    return render(request, "main_app/esewa_successful.html")