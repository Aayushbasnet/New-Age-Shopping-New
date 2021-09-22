from main_app.models import *
from django import forms


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        # fields = "__all__"
        exclude = ('product_quantity',
                   'product_discount', 'slug', 'user')


class ProductDiscountForm(forms.ModelForm):
    class Meta:
        model = ProductDiscount
        exclude = ('slug',)


class ProductInventoryForm(forms.ModelForm):
    class Meta:
        model = ProductInventory
        exclude = ('slug','product_inventory_name')

class MerchantProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'pan_number', 'document')