from django.contrib import admin
from .models import *

# Register your models here.
#my profile admin
@admin.register(MyProfile)
class MyProfileAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'user', 'shipping_address', 'mobile']


#review seller admin
@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'full_name', 'receiver_no', 'region', 'city', 'area', 'address', 'label']

#review seller admin
@admin.register(ReviewSeller)
class ReviewSellerAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'user', 'rate', 'is_rated', 'order_items', 'rated_date']
