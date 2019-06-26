from django.shortcuts import render
from productAdd.models import Product,Order

from user.models import Profile
from productAdd.models import Product
# *****************************************************************
from django.utils import timezone
from productAdd.forms import ProductForm
from productAdd.models import Delivery
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required

# ////////////////////////////////////////////////////////////////////
# Create your views here.
def cart(request):
    return render(request,'cart/cart.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'cart/product_detail.html'

        
class OrderHistoryListView(ListView):
    model = Order
    template_name = 'cart/order_history.html'  # <app>/<model>_<viewtype>.html
    queryset = Order.objects.all()
    context_object_name = 'order_list'

    def get_queryset(self):
        # if (productAdd.Product not None):
        # if(None not in Order.products.all()):
        return Order.objects.filter(status="deactivate").filter(user=self.request.user)

@login_required    
def removeFromCart(request,):    
    product =  get_object_or_404(Product, id=request.POST.get('product_id'))
    #add_cart = True
    user = request.user
    print(user)
    profile = Profile.objects.get(user= user)
    # *************************************
    print(profile.cart.all())
    print(user)
    # *************************************
    if(product in profile.cart.all()):
        print("product removed from cart")
        profile.cart.remove(product)
        #add_cart = False    
    return HttpResponseRedirect(product.get_url())

@login_required
def checkout(request, pk):
    delivery = Delivery.objects.get(id = pk)
    print("*******************************************************")
    print(delivery.id)
    print("*******************************************************")
    user = request.user
    order = Order()
    order.user = user
    profile = Profile.objects.get(user= user)
    amount=profile.get_cart_total()
    for item in profile.cart.all():
        order.product=item
        order.total_amount=profile.get_cart_total()
        order.delivery = delivery
        order.order_date= timezone.now()
        # order.delivery_date = timezone.now()
        order.status = "active"
        order.save()        
        profile.cart.remove(item)
    # cart = profile.cart.all()
    # *******************************************************
    import smtplib 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("aleenav1996@gmail.com", "sweetchurch") 
    
    # message = "Rs"+ amount +"is debited from your account"
    your_message = "Rs {} is debited from your account".format(amount)
    dest = user.email
    print("*************************")
    print(order.order_date)
    print(your_message)
    s.sendmail("aleenav1996@gmail.com", dest , your_message) 
    print("success")
    # terminating the session 
    s.quit()
    # ******************************************************* 
    return HttpResponseRedirect(profile.get_checkout_url())

# @login_required
# def checkout(request):
#     user = request.user
#     profile = Profile.objects.get(user= user)

#     # cart = profile.cart.all()
#     # *******************************************************
#     import smtplib 
#     s = smtplib.SMTP('smtp.gmail.com', 587) 
#     s.starttls() 
#     s.login("aleenav1996@gmail.com", "sweetchurch") 
#     amount=profile.get_cart_total()
#     # message = "Rs"+ amount +"is debited from your account"
#     your_message = "Rs{} is debited from your account".format(amount)
#     dest = user.email
#     print(dest)
#     print(your_message)
#     s.sendmail("aleenav1996@gmail.com", dest , your_message) 
#     print("success")
#     # terminating the session 
#     s.quit()
#     # ******************************************************* 
#     return HttpResponseRedirect(profile.get_checkout_url())

