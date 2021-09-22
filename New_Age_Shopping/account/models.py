from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from uuid import uuid4
from random import randint


class User(AbstractUser):
    # def image_rename(self, filename):
    #     upload_to = self.usernaem + "/"
    #     # file_extension       =   filename.split(".")[-1]
    #     product_name = self.user
    #     png_file_extension = "png"

    #     # get filename
    #     if product_name:
    #         print(self.id)
    #         filename = '{}{}.{}'.format(
    #             product_name, str(uuid4().hex), png_file_extension)
    #     else:
    #         filename = '{}.{}'.format(uuid4().hex, png_file_extension)

    gender = [
        ("Male", 'Male'),
        ("Female", 'Female'),
        ("Other", 'Other')
    ]
    phone_number = PhoneNumberField(region="NP")
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, choices=gender)
    is_customer = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)
    pan_number = models.BigIntegerField("Merchant Pan Number", unique=True, blank=True, null=True)
    document = models.ImageField("Merchant Document Image", upload_to= "Documents")

    def __str__(self):
        return self.username
