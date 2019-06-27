from django.urls import path
from . import views

# #set namespace
app_name = 'home'
urlpatterns=[
    path('',views.index,name='index'),
    ]
