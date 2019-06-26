from django import forms
from .models import Profile, Product, Feedbacks
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    address = forms.CharField(required=False) 

    class Meta:
        model = Profile
        
        fields = ['address','contact_number','alternate_contact_number']

class FeedbackForm(forms.ModelForm):    
    class Meta:        
        model = Feedbacks        
        fields = ['title','message']


