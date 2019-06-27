from django.db import models
from django.contrib.auth.models import User
from productAdd.models import Product
# from django.contrib.postgres.fields import JSONField

from decimal import Decimal
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    address = models.CharField(max_length=50, null=True)
    contact_number = models.BigIntegerField(null=False, blank=False, unique=True)
    alternate_contact_number = models.BigIntegerField(null=False, blank=False, unique=True)
    cart = models.ManyToManyField(Product, default = 0, related_name='cart', blank=True)
    # wishlist = models.ManyToManyField(Product, default = 0, related_name='wishlist', blank=True)
    # quantity = JSONField()

    def __str__(self):
        return f'{ self.user.username } Profile'
        
    # @receiver(post_save, sender=User)
    # def create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_Profile(sender, instance, **kwargs):
    #     try:
    #         instance.Profile.save()
    #     except:
    #         pass

    def get_cart_total(self):
        total = Decimal(0.000)
        for product in self.cart.all():
            if product in Product.objects.all():                                
                total +=product.price            
        return(total)
          
    def get_checkout_url(self):
        return reverse('productAdd:listproducts')

class Feedbacks(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    # user = models.OneToOneField(User, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.title

# class Delivery(models.Model):
#     user = models.ForeignKey(User, on_delete= models.CASCADE)
#     person =  models.CharField(max_length=50)
#     contact_number = models.BigIntegerField(null=False, blank=False, unique=True)
#     address = models.CharField(max_length=50, null=True)
#     postal_code = models.BigIntegerField(null=False, blank=False)

#     def __str__(self):
#         return self.person