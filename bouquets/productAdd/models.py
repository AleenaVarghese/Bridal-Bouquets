from django.db import models
from productAdd.choices import *
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    bouqet_type = models.IntegerField(choices=BOUQUETS_CHOICES, default=1)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    flower_type = models.IntegerField(choices=FLOWER_CHOICES, default=1)
    image = models.ImageField(upload_to='product_pics', null=False)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('productAdd:listproducts')

    def get_url(self):
        return reverse('cart:cart')

class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    person =  models.CharField(max_length=50)
    contact_number = models.BigIntegerField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=50, null=True)
    postal_code = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return self.person

class Order(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE, blank=True)
    delivery = models.ForeignKey(Delivery, on_delete= models.CASCADE, blank=True)
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10,decimal_places=3)
    delivery_date = models.DateTimeField(null=True)
    cancel_order = models.CharField(max_length=100,null= False)
    status = models.CharField(max_length=100,null= False, blank=True)#not blank

    def get_absolute_url(self):
        return reverse('productAdd:listproducts')

# class Order(models.Model):
#     user = models.OneToOneField(User, on_delete= models.CASCADE)
#     products = models.ManyToManyField(Product, default = 0, related_name='products', blank=True)
#     order_date = models.DateTimeField(auto_now=True)





