from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


# Product admin.
class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    list_display    =   ['id', 'user','product_category','product_name', 'product_price',  'product_quantity', 'product_availability', 'product_discount', 'product_image_src']
    summernote_fields = ('product_description','product_short_description',)

admin.site.register(Product, ProductAdmin)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    exclude =('slug',)
    list_display    =   ['id', 'category_name_level2', 'product_category_description']

@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    exclude =('slug',)
    list_display    =   ['id', 'product_inventory_name', 'product_inventory_quantity']

@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    exclude =('slug',)
    list_display    =   ['id', 'product_discount_name', 'product_discount_active', 'product_discount_description', 'product_discount_percentage']

@admin.register(FeaturedSliderProduct)
class FeaturedSliderProductAdmin(admin.ModelAdmin):
    list_display    =   ['featured_product_name', 'featured_product_description', 'featured_product_active', 'featured_product_image','created_at']

#level 1 product category admin
@admin.register(Level1ProductCategory)
class Level1ProductCategoryAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'category_level1']

#level 2 product category admin
@admin.register(Level2ProductCategory)
class Level2ProductCategoryAdmin(admin.ModelAdmin):
    exclude =('slug',)
    list_display    =   ['id', 'category_level2']


#order admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'user', 'date_ordered', 'transcation_id', 'complete']


#order items
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'user', 'product', 'order', 'quantity', 'shipping_address', 'payment', 'complete', 'being_delivered', 'received', 'added_date']


#shipping address
@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'user', 'first_name', 'last_name', 'email', 'phone_number','shipping_district', 'shipping_address', 'shipping_zip', 'payment_option', 'checkout_date']

#comment admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'status', 'user', 'product', 'subject', 'comment', 'rate', 'create_at', 'ip']


#Alternative images admin
@admin.register(ProductAlternativeImages)
class ProductAlternativeImagesAdmin(admin.ModelAdmin):
    list_display = ['alternative_image']  

#Payment admin
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'stripe_charge_id', 'user', 'amount', 'timestamp']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display    =   ['id', 'full_name', 'phone_number', 'email', 'messages', 'seen']


