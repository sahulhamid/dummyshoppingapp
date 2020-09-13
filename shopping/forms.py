from django import forms

from .models import Product,Profile
from django.contrib.auth.models import User

class AddProducts(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class RegisterFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        #fields = ['first_name','last_name','address','phone_number']
        fields = '__all__'