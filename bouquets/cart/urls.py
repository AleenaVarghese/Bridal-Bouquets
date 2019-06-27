from django.urls import path
from . import views
from .views import ProductDetailView, OrderHistoryListView, OrderDetailView

# #set namespace
app_name = 'cart'

urlpatterns = [
    path('',views.cart, name='cart'),  
    path('<int:pk>/checkout',views.checkout, name='checkout'),  
    path('removeFromCart/',views.removeFromCart, name='removeFromCart'),  
    path('<int:pk>/', ProductDetailView.as_view(), name='cart_detail'), 
    path('orderDetail', OrderDetailView.as_view(), name='order_detail'), 
    path('cancelOrder', views.CancelOrder, name='cancel_order'), 
    path('order_history/',views.OrderHistoryListView.as_view(), name='order_history'),   
]


