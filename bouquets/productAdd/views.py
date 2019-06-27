from django.shortcuts import render
from productAdd.forms import ProductForm, DeliveryForm
from .models import Product, Order,Delivery
from user.models import Profile
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.urls import reverse_lazy

# Create your views here.
class ProductCreateView(CreateView):
        model = Product        
        template_name = 'productAdd/addnew.html'
        form_class = ProductForm #it is a variable so don't use quotes.
        success_url = '../'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('productAdd:listproducts')

class OrderListView(ListView):
    model = Order
    template_name = '/productAdd/order_list.html'  # <app>/<model>_<viewtype>.html
    queryset = Order.objects.all()
    context_object_name = 'order_list'
    # paginate_by = 6

    def get_queryset(self):
        return Order.objects.filter(status="active").filter(cancel_order="notcanceled")


class ProductListView(ListView):
    model = Product
    template_name = '/productAdd/product_list.html'  # <app>/<model>_<viewtype>.html
    queryset = Product.objects.all()
    context_object_name = 'Product_list'    

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailView(DetailView):
    model = Product
    # template_name = '/productAdd/product_detail.html'

class DeliveryCreateView(CreateView):
        model =  Delivery         
        template_name = 'user/delivery.html'
        form_class = DeliveryForm #it is a variable so don't use quotes.
        # success_url = '../cart/checkout'
        # success_url = reverse_lazy('cart:checkout')

        def form_valid(self, form):
            form.instance.user = self.request.user            
            return super(DeliveryCreateView, self).form_valid(form)
        
        def get_success_url(self):
            return reverse_lazy('cart:checkout', kwargs={'pk': self.object.pk})

def approve_delivery(request,):    
    order =  get_object_or_404(Order, id=request.POST.get('order_id'))    
    user = order.user
    order.status = "deactivate"
    order.delivery_date = timezone.now()
    order.save()            
    # *******************************************************
    import smtplib 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("aleenav1996@gmail.com", "sweetchurch") 
    
    your_message = "Product is delivered succesfully"
    dest = user.email
    print("*************************")
    print(order.order_date)
    print(your_message)
    s.sendmail("aleenav1996@gmail.com", dest , your_message) 
    print("success")
    # terminating the session 
    s.quit()
    # ******************************************************* 
    return HttpResponseRedirect(order.get_absolute_url())


@login_required    
def addtoCart(request,):    
    product =  get_object_or_404(Product, id=request.POST.get('product_id'))
    # add_cart = False
    user = request.user
    print(user)
    profile = Profile.objects.get(user= user)
    # *************************************
    print(profile.cart.all())
    print(user)
    # *************************************
    if(product not in profile.cart.all()):
        print("product added to cart")
        profile.cart.add(product)
        # add_cart= True    
    # return redirect('productAdd:listproducts')
    return HttpResponseRedirect(product.get_absolute_url())

# class OrderHistoryListView(ListView):
#     model = Order
#     template_name = '/productAdd/order_history.html'  # <app>/<model>_<viewtype>.html
#     queryset = Order.objects.all()
#     context_object_name = 'order_list'

#     def get_queryset(self):
#         # if (productAdd.Product not None):
#         # if(None not in Order.products.all()):
#         return Order.objects.filter(status="deactivate")


# @login_required    
# def removeFromCart(request,):    
#     product =  get_object_or_404(Product, id=request.POST.get('product_id'))
#     add_cart = True
#     user = request.user
#     print(user)
#     profile = Profile.objects.get(user= user)
#     # *************************************
#     print(profile.cart.all())
#     print(user)
#     # *************************************
#     if(product in profile.cart.all()):
#         print("product removed from cart")
#         profile.cart.remove(product)
#         add_cart = False
#     else:
#         # print("product added to cart")
#         # profile.cart.add(product)
#         # add_cart= True
#         pass
#     # return redirect('productAdd:listproducts')
#     return HttpResponseRedirect(product.get_absolute_url())

# def search_product(request):
#     if(request.method == 'GET'):
#         item = request.Get('search')
#         search_item = Product.req

# def search_product(request):
#     qs = Product.objects.all()
#     search_product = request.GET.get('search-product')
#     context={
#         'queryset':qs
#     }
#     return render(request,"/productAdd/search_product.html", context)


# class ProductSearchView(ListView):
#     model = Product
#     template_name = '/productAdd/search_product.html'  # <app>/<model>_<viewtype>.html
#     queryset = Product.objects.filter(title__icontains='beautiful')
#     context_object_name = 'product_list'

#     def get_queryset(self):
#         try:
#             name = self.kwargs['title']
#         except:
#             name = ''
#         if (name != ''):
#             object_list = self.product.objects.filter(title__icontains='beautiful')
#         else:
#             object_list = self.model.objects.all()
#         return object_list
