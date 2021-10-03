from main_app.models import *
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.exceptions import ValidationError


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

    def clean_pan_number(self):
        pan_number = self.cleaned_data['pan_number']
        if len(str(pan_number)) != 9:
            raise ValidationError("Pan number must be 9 digits")
        print(pan_number)
        return pan_number

# class AlternativeImageForm(forms.ModelForm):
#     class Meta:
#         model =  ProductAlternativeImages
#         fields = ('alternative_image1',)