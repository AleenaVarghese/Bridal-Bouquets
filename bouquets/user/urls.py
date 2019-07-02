from django.urls import path
from . import views
from .views import FeedbackCreateView, FeedbackListView
from django.contrib.auth import views as auth_views

# #set namespace
app_name = 'user'

urlpatterns = [
    path('register',views.register, name='register'),  
    # path('feedback',views.Feedback, name='feedback'),  
    path('feedback',views.FeedbackCreateView.as_view(), name='feedback'),         
    path('feedback_list/',views.FeedbackListView.as_view(), name='feedback_list'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'), 
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'), 
]