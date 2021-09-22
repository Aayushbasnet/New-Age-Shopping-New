from main_app.models import *
from django import forms


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        # fields = "__all__"
        exclude = ('product_quantity',
                   'product_discount', 'slug')
        labels = {
            'product_category': 'Brand Name'
        }


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        exclude = ('slug','brand_name', 'product_category_description')


class Lvl2Category(forms.ModelForm):
    class Meta:
        model = Level2ProductCategory
        exclude = ('category_level2', 'slug')


class ProductDiscountForm(forms.ModelForm):
    class Meta:
        model = ProductDiscount
        exclude = ('slug',)


class ProductInventoryForm(forms.ModelForm):
    class Meta:
        model = ProductInventory
        exclude = ('slug','product_inventory_name')
