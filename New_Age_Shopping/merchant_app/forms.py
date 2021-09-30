from main_app.models import *
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        # fields = "__all__"
        exclude = ('product_quantity',
                   'product_discount', 'slug', 'user')
                   
        widgets = {
            'product_short_description': SummernoteWidget(),
            'product_description': SummernoteWidget(),
        }


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

# class AlternativeImageForm(forms.ModelForm):
#     class Meta:
#         model =  ProductAlternativeImages
#         fields = ('alternative_image1',)