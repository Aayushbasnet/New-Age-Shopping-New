from django.db import models
from account.models import User
from phonenumber_field.modelfields import PhoneNumberField
from main_app.models import OrderItem

# Create your models here.
SHIPPING_ADDRESS = (
    ('Office', 'Office'),
    ('Home', 'Home'),
)

class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=100)
    receiver_no = PhoneNumberField(region='NP')
    region = models.CharField(max_length=100)
    city   = models.CharField(max_length=100)
    area   = models.CharField(max_length=100)
    address = models.CharField(max_length=100, help_text="House# 001")
    label   = models.CharField(max_length=8, choices=SHIPPING_ADDRESS)

    def __str__(self):
        return f'({self.full_name})-{self.area}'

    class Meta:
        verbose_name_plural = 'Shipping Addresses'

class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    mobile = PhoneNumberField(region='NP')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'Customer Profile'

class ReviewSeller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField()
    is_rated = models.BooleanField(default=False)
    order_items = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)
    rated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + str(self.rate) 