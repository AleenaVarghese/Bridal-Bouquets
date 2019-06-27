from django.urls import path
from . import views
from .views import ProductCreateView, ProductListView, ProductDetailView, OrderListView, ProductDeleteView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# #set namespace
app_name = 'productAdd'

urlpatterns = [
    path('add',views.ProductCreateView.as_view(), name='addproducts'), 
    path('listproducts/',views.ProductListView.as_view(), name='listproducts'),
    path('listorder/',views.OrderListView.as_view(), name='order_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='cart_detail'),  
    path('cart/',views.addtoCart, name='addtoCart'),
    # path('search/',views.search_product, name='search_product'),
    path('delivery',views.DeliveryCreateView.as_view(), name='delivery'),   
    path('approve_delivery/',views.approve_delivery, name='approve_delivery'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 