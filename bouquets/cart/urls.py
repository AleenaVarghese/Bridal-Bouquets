from django.urls import path
from . import views
from .views import ProductDetailView, OrderHistoryListView

# #set namespace
app_name = 'cart'

urlpatterns = [
    path('',views.cart, name='cart'),  
    path('<int:pk>/checkout',views.checkout, name='checkout'),  
    path('removeFromCart/',views.removeFromCart, name='removeFromCart'),  
    path('<int:pk>/', ProductDetailView.as_view(), name='cart_detail'), 
    path('order_history/',views.OrderHistoryListView.as_view(), name='order_history'),   
]


