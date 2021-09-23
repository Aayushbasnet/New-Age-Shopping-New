from django.shortcuts import render, redirect
from .forms import *
from main_app.models import Product, ProductDiscount, ProductInventory, Level1ProductCategory
# from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from account.models import User
from django.contrib.auth import logout


def merchantDashboard(request):
    add_product = AddProduct()
    product_discount = ProductDiscountForm()
    product_inventory = ProductInventoryForm()

    if request.method == "POST":
        add_product = AddProduct(request.POST or None, request.FILES)
        product_discount = ProductDiscountForm(request.POST or None)
        product_inventory = ProductInventoryForm(request.POST or None)
        print("I am inside post")

        if add_product.is_valid() and product_discount.is_valid() and product_inventory.is_valid():
            print("valid")
            add_product.save(commit = False)
        #     print("I am saved")

            #add_product
            product_name = add_product.cleaned_data.get('product_name')
            # print(product_name)
            product_desc = add_product.cleaned_data.get('product_description')
            # print(product_desc)
            product_price = add_product.cleaned_data.get('product_price')
            # print(product_price)
            product_availability = add_product.cleaned_data.get('product_availability')
            # print(product_availability)
            product_image = add_product.cleaned_data.get('product_image_src')
            # print(product_image)
            product_category = add_product.cleaned_data.get('product_category')

            # product_discount
            product_discount_active = product_discount.cleaned_data.get('product_discount_active')
            # print(product_discount_active)
            product_discount_name = product_discount.cleaned_data.get('product_discount_name')
            # print(product_discount_name)
            product_discount_desc = product_discount.cleaned_data.get('product_discount_description')
            # print(product_discount_desc)
            product_discount_percentage = product_discount.cleaned_data.get('product_discount_percentage')
           
           # product_inventory
            product_inventory_quantity = product_inventory.cleaned_data.get('product_inventory_quantity')


            product_discount_obj = ProductDiscount.objects.create(
                product_discount_active = product_discount_active,
                product_discount_name = product_discount_name,
                product_discount_description = product_discount_desc,
                product_discount_percentage = product_discount_percentage
            )

            product_inventory_obj = ProductInventory.objects.create(
                product_inventory_name = str(product_name) , 
                product_inventory_quantity = product_inventory_quantity
            )

            print(product_inventory_obj)


            product_obj = Product.objects.create(
                user = request.user,
                product_name = product_name,
                product_description = product_desc,
                product_price = product_price,
                product_availability = product_availability,
                product_discount = product_discount_obj,
                product_quantity = product_inventory_obj,
                product_image_src = product_image,
                product_category = product_category,
            )
            product_obj.save()
            return HttpResponseRedirect('./')

        else:
            print("Invalid form")
            # pass



    merchants_product = Product.objects.filter(user = request.user)

    #show profile
    merchant_user = User.objects.get(id = request.user.pk)
    print(merchant_user)

    #for low stock
    low_stock = merchants_product.filter(product_quantity__product_inventory_quantity__lte = 5).count() 
    print(low_stock)

    context = {
        'add_product' : add_product,
        'product_discount' : product_discount,
        'product_inventory' : product_inventory,
        'merchants_product' : merchants_product,
        'merchant_user' : merchant_user,
        'low_stock' : low_stock,
    }

    return render(request, 'merchant_app/mHomepage.html', context)

    

def delete_product(request, id):
    delete_merchant_product = Product.objects.get(pk = id)
    delete_merchant_product.delete()
    return redirect('/merchant/#v-pills-profile/')

def update_product(request, id):
    update_merchant_product = Product.objects.get(id = id)

    product_inventory_getter = ProductInventory.objects.all()
    print(product_inventory_getter)
    update_mechant_product_inventory = product_inventory_getter.get(quantity__id = id)
    print(update_mechant_product_inventory)

    product_discount_getter = ProductDiscount.objects.all()
    if update_merchant_product.product_discount and update_merchant_product.product_discount.product_discount_active:
        update_merchant_product_discount = product_discount_getter.get(discount__id = id)
        product_discount = ProductDiscountForm(instance=update_merchant_product_discount)
        print(update_mechant_product_inventory)
    else:
        update_merchant_product_discount = product_discount_getter.get(discount__id = id)
        product_discount = ProductDiscountForm()
        print(update_mechant_product_inventory)
    

    add_product = AddProduct(instance= update_merchant_product)
    product_inventory = ProductInventoryForm(instance= update_mechant_product_inventory)

    if request.method == "POST":
        add_product = AddProduct(request.POST, request.FILES, instance= update_merchant_product)
        product_inventory = ProductInventoryForm(request.POST, instance= update_mechant_product_inventory)
        if update_merchant_product.product_discount and update_merchant_product.product_discount.product_discount_active:
            update_merchant_product_discount = product_discount_getter.get(discount__id = id)
            product_discount = ProductDiscountForm(request.POST, instance=update_merchant_product_discount)
            print(update_mechant_product_inventory)
        else:
            update_merchant_product_discount = product_discount_getter.get(discount__id = id)
            product_discount = ProductDiscountForm(request.POST, instance=update_merchant_product_discount)
            print(update_mechant_product_inventory)

        if add_product.is_valid() and product_inventory.is_valid() and product_discount.is_valid():
            add_product.save()
            product_inventory.save()
            product_discount.save() 
            return redirect('/merchant/#v-pills-product')
        else:
            print("Not valid")           



    context = {
        'add_product' : add_product,
        'product_discount' : product_discount,
        'product_inventory' : product_inventory,
    }

    return render(request, 'merchant_app/mUpdate_product.html', context)


def mProfileUpdate(request):
    update_profile = MerchantProfileForm(instance = request.user)
    if request.method == "POST":
        update_profile = MerchantProfileForm(request.POST,request.FILES, instance = request.user)
        if update_profile.is_valid():
            update_profile.save()
            return redirect('/merchant/')
        else:
            print(update_profile)
            print("Form invalid")
    else:
        print("POST Invalid")        
    context ={
        'update_profile' : update_profile,
    }
    return render(request, 'merchant_app/mUpdateProfile.html', context)

def mlogout(request):
    logout(request)
    return redirect('/account/login/')