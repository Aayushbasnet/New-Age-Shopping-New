from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from uuid import uuid4
from random import randint
from django.db.models import Avg


class User(AbstractUser):
    gender = [
        ("Male", 'Male'),
        ("Female", 'Female'),
        ("Other", 'Other')
    ]
    phone_number = PhoneNumberField(region="NP")
    shop_name = models.CharField(max_length = 150)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, choices=gender)
    is_customer = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)
    pan_number = models.BigIntegerField("Merchant Pan Number", unique=True, null=True)
    document = models.ImageField("Merchant Document Image", upload_to= "Documents")

    def __str__(self):
        return self.username


