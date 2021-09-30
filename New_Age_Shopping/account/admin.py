from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display    =   ['username', 'phone_number', 'email', 'address', 'gender','is_customer', 'is_merchant', 'is_superuser', 'pan_number', 'document']