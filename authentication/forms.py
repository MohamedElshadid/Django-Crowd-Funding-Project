from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    phone = forms.CharField(max_length=200, help_text='Required')
    image=forms.ImageField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2','first_name','last_name','image','phone')
    