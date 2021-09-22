from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display    =   ['product_category','product_name', 'product_description','product_price',  'product_quantity', 'product_availability', 'product_discount', 'product_image_src']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display    =   ['category_name_level2', 'product_category_description']

@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display    =   ['product_inventory_name', 'product_inventory_quantity']

@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display    =   ['product_discount_name', 'product_discount_active', 'product_discount_description', 'product_discount_percentage']

@admin.register(FeaturedSliderProduct)
class FeaturedSliderProductAdmin(admin.ModelAdmin):
    list_display    =   ['featured_product_name', 'featured_product_description', 'featured_product_active', 'featured_product_image']

admin.site.register(Level1ProductCategory)
admin.site.register(Level2ProductCategory)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)






