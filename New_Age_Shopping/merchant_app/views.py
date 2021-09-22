from django.shortcuts import render
from .forms import *
from main_app.models import Product, ProductDiscount, ProductInventory, ProductCategory, Level2ProductCategory, Level1ProductCategory
# from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect

def merchantDashboard(request):
    add_product = AddProduct()
    product_category_form = ProductCategoryForm()
    lvl_2_pc = Lvl2Category()
    product_discount = ProductDiscountForm()
    product_inventory = ProductInventoryForm()

    if request.method == "POST":
        add_product = AddProduct(request.POST or None, request.FILES)
        product_category_form = ProductCategoryForm(request.POST or None)
        lvl_2_pc = Lvl2Category(request.POST or None)
        product_discount = ProductDiscountForm(request.POST or None)
        product_inventory = ProductInventoryForm(request.POST or None)
        # print("I am inside post")

        if add_product.is_valid() and product_category_form.is_valid() and lvl_2_pc.is_valid() and product_discount.is_valid() and product_inventory.is_valid():
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
            brand_name = add_product.cleaned_data.get('product_category')
            # print(brand_name)
            

            #lvl_2_pc
            lvl_1_pc = lvl_2_pc.cleaned_data.get('category_name_level1')
            # print(lvl_1_pc)

            #product_category
            level_2_pc = product_category_form.cleaned_data.get('category_name_level2')
            # print(level_2_pc)

            # product_discount
            product_discount_active = product_discount.cleaned_data.get('product_discount_active')
            # print(product_discount_active)
            product_discount_name = product_discount.cleaned_data.get('product_discount_name')
            # print(product_discount_name)
            product_discount_desc = product_discount.cleaned_data.get('product_discount_description')
            # print(product_discount_desc)
            product_discount_percentage = product_discount.cleaned_data.get('product_discount_percentage')
            # print(product_discount_percentage)
           
           # product_inventory
            product_inventory_quantity = product_inventory.cleaned_data.get('product_inventory_quantity')
            # print(product_inventory_quantity)

            product_category_obj = ProductCategory.objects.get(
                brand_name = brand_name
            )

            product_discount_obj = ProductDiscount.objects.create(
                product_discount_active = product_discount_active,
                product_discount_name = product_discount_name,
                product_discount_description = product_discount_desc,
                product_discount_percentage = product_discount_percentage
            )

            product_inventory_obj = ProductInventory.objects.create(
                product_inventory_name = str(product_name) + "--" + str(brand_name) + "--" + str(level_2_pc) + "--" + str(lvl_1_pc), 
                product_inventory_quantity = product_inventory_quantity
            )

            print(product_inventory_obj)


            product_obj = Product.objects.create(
                product_name = product_name,
                product_description = product_desc,
                product_price = product_price,
                product_availability = product_availability,
                product_discount = product_discount_obj,
                product_quantity = product_inventory_obj,
                product_image_src = product_image,
                product_category = product_category_obj,
            )
            product_obj.save()
            return HttpResponseRedirect('./')

        else:
            print("Invalid form")
            # pass

    context = {
        'add_product' : add_product,
        'product_category' : product_category_form,
        'lvl_2_pc' : lvl_2_pc,
        'product_discount' : product_discount,
        'product_inventory' : product_inventory,
    }

    return render(request, 'merchant_app/mHomepage.html', context)


def delete_product(request):
    return render(request, 'merchant_app/delete_product.html')

def edit_product(request):
    return render(request, 'merchant_app/edit_product.html')
