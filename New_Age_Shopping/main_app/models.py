from django.db import models
import os
from uuid import uuid4
from random import randint
from django.db.models.aggregates import Count
# from django.contrib.auth.models import User
from account.models import User
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import Avg



class ProductBaseClass(models.Model):
    created_at      =   models.DateTimeField(auto_now_add=True)
    modified_at     =   models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Level1ProductCategory(ProductBaseClass):
    category_level1 =   models.CharField(max_length=150, unique=True, help_text='Level1 category like electronics, health and beauty, sports and entertainment')

    def __str__(self):
        return str(self.category_level1)

    class Meta:
        verbose_name_plural = 'Level 1 Categories'

    def save(self, *args, **kwargs):
        self.category_name_level1 = self.category_level1.upper()
        return super().save(*args, **kwargs)

    @property
    def level2_item(self):
        # print("hello world")
        first_level_item    =   Level1ProductCategory.objects.get(pk = self.pk)
        second_level_item   =   Level2ProductCategory.objects.filter(category_name_level1 = first_level_item)
        # print(first_level_item)
        return second_level_item


class Level2ProductCategory(ProductBaseClass):
    category_name_level1       =    models.ForeignKey(Level1ProductCategory, on_delete=models.CASCADE)
    category_level2            =    models.CharField(max_length=150, unique=True, help_text='s Level2 like mobiles, laptop, soap etc.')
    
    slug    =   models.SlugField(max_length=300,blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.category_level2)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.category_level2)
    
    class Meta:
        verbose_name_plural = 'Level 2 Categories'

    def save(self, *args, **kwargs):
        self.category_name_level2 = self.category_level2.upper()
        return super().save(*args, **kwargs)

    def level3_item(self):
        second_level_item   =   Level2ProductCategory.objects.get(pk = self.pk)
        third_level_item    =   ProductCategory.objects.filter(category_name_level2 = second_level_item)
        return third_level_item
        

class ProductCategory(ProductBaseClass):
    category_name_level2            =   models.ForeignKey(Level2ProductCategory, on_delete=models.CASCADE)
    brand_name                      =   models.CharField(max_length=100)
    product_category_description    =   models.CharField(max_length=250, blank=True, null=True)
    slug    =   models.SlugField(max_length=300,blank=True,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.brand_name)

    class Meta:
        verbose_name            =   'Product Category'
        verbose_name_plural     =   'Product Categories'
    

class ProductInventory(ProductBaseClass):
    product_inventory_name      =   models.CharField(max_length=180, blank=True, null=True)
    product_inventory_quantity  =   models.IntegerField(default=1)

    slug    =   models.SlugField(max_length=300,blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.product_inventory_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{} {} {}'.format(self.product_inventory_name, ", quantity- ", self.product_inventory_quantity)

class ProductDiscount(ProductBaseClass):
    product_discount_active         =   models.BooleanField(default=False, blank=True, null=True)
    product_discount_name           =   models.CharField(max_length=180, blank=True, null=True)
    product_discount_description    =   models.CharField(max_length= 250, blank=True, null=True)
    product_discount_percentage     =   models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    slug    =   models.SlugField(max_length=300,blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.product_discount_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.product_discount_name)  


class FeaturedSliderProduct(ProductBaseClass):
   
    # to change name of product image
    def image_rename(self, filename):
        upload_to              =   "featuredProudct/"
        # file_extension          =   filename.split(".")[-1]
        featured_product_name  =   self.featured_product_name
        png_file_extension     =   "png"

        #get filename
        if featured_product_name:
            print(self.id)
            filename    =   '{}{}.{}'.format(featured_product_name, str(uuid4().hex), png_file_extension)
        else:
            filename    =   '{}.{}'.format(uuid4().hex, png_file_extension)

        #return the whole path and file
        return os.path.join(upload_to, filename)

    featured_product_name           =   models.CharField(max_length = 180)

    def save(self, *args, **kwargs):
        self.featured_product_name = self.featured_product_name.upper()
        return super(FeaturedSliderProduct, self).save(*args, **kwargs)


    featured_product_description    =   models.CharField(max_length = 200) 
    featured_product_active         =   models.BooleanField(default=True)
    featured_product_image          =   models.ImageField("Featured Product Image", upload_to= image_rename)  

class Product(ProductBaseClass):
    # to change name of product image
    def image_rename(self, filename):
        upload_to              =   self.product_category.category_name_level2.category_level2 +"/"
        # file_extension       =   filename.split(".")[-1]
        product_name           =   self.product_name
        png_file_extension     =   "png"

        #get filename
        if product_name:
            print(self.id)
            filename    =   '{}{}.{}'.format(product_name, str(uuid4().hex), png_file_extension)
        else:
            filename    =   '{}.{}'.format(uuid4().hex, png_file_extension)

        #return the whole path and file
        return os.path.join(upload_to, filename)
    user                        =   models.ForeignKey(User, on_delete=models.CASCADE)
    product_name                =   models.CharField(max_length=500)
    product_short_description   =   models.TextField()
    product_description         =   models.TextField()
    product_price               =   models.DecimalField(max_digits=8, decimal_places=2)
    product_availability        =   models.BooleanField(default=True)
    product_discount            =   models.ForeignKey(ProductDiscount, on_delete=models.CASCADE, blank=True, null=True, related_query_name='discount')
    product_quantity            =   models.ForeignKey(ProductInventory, on_delete= models.CASCADE, related_query_name= 'quantity')
    product_image_src           =   models.ImageField("Product Image", upload_to= image_rename)
    product_category            =   models.ForeignKey(ProductCategory, on_delete= models.CASCADE)
    
    # random_product_selector     =   ProductManager()

    slug    =   models.SlugField(max_length=300,blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.product_name)

    # to calculate product discount
    @property
    def discount_calculator(self):
        pk_object= Product.objects.get(pk=self.pk)
        price_after_discount = float(self.product_price-(pk_object.product_discount.product_discount_percentage*1/100*self.product_price))
        return '%.2f'%price_after_discount

    @property
    def average_product_rating(self):
        reviews = Comment.objects.filter(product = self).aggregate(rating_avg =Avg("rate"))
        return reviews
        

    # class Meta:
    #     constraints = [models.CheckConstraint(check=models.Q(product_price__gte=18), name="price_constraints")] 



class Order(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date_ordered    =   models.DateTimeField(auto_now_add=True)
    transcation_id  =   models.CharField(max_length=100 , null=True)
    complete    =   models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, blank=True, null=True)
    quantity =  models.IntegerField(default=1, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    complete    =   models.BooleanField(default=False)
    shipping_address = models.ForeignKey('ShippingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-added_date"]

    @property
    def get_total(self):
        if self.product.product_quantity.product_inventory_quantity > 0:
            if self.product.product_discount and self.product.product_discount.product_discount_active:
                price = self.product.discount_calculator
                item_total = float(price) * self.quantity
                return item_total
            else:
                price = self.product.product_price
                item_total = price* self.quantity
                return item_total
        else:
            item_total = 0
            return item_total

    
    def __str__(self):
        return str(self.product)


class ShippingAddress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True, region='NP')
    shipping_district = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    shipping_zip = models.CharField(max_length=200, blank=True, null=True)
    payment_option = models.CharField(max_length=200)
    checkout_date = models.DateTimeField(auto_now_add=True)
    payment_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.shipping_address)

    class Meta:
        verbose_name_plural = 'Shipping Addresses'
        ordering = ("-payment_update",)

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )

    SUBJECT_CHOICES = (
    ('Best', 'Best'),
    ('Average', 'Average'),
    ('Poor','Poor')
    )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_query_name='product_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=25, choices=SUBJECT_CHOICES, default = 'Best', blank=True)
    comment = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default = 'New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ("-create_at",)
 

class ProductAlternativeImages(models.Model):
    # to change name of product image
    def image_rename(self, filename):
        upload_to              =   "Alternative_images/"+ str(self.product.product_category)+"/"+self.product.product_name
        # file_extension       =   filename.split(".")[-1]
        product_name           =   self.product.product_name
        png_file_extension     =   "png"

        #get filename
        if product_name:
            print(self.id)
            filename    =   '{}{}.{}'.format(product_name, str(uuid4().hex), png_file_extension)
        else:
            filename    =   '{}.{}'.format(uuid4().hex, png_file_extension)

        #return the whole path and file
        return os.path.join(upload_to, filename)

    alternative_image = models.ImageField("Product Image", upload_to= image_rename)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.product_name)+ " alternative-images"

    class Meta:
        verbose_name_plural = 'Alternative Image'

class ContactUs(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(region='NP')
    messages = models.TextField()
    seen = models.BooleanField(default=False)
    messaged_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.full_name)+ str(self.phone_number)

    class Meta:
        verbose_name_plural = 'Contact Us'

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ["-timestamp"]