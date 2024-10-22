from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Registration form for new users
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    class Meta:
        model = User
        fields = ['username','email','phone_no','password1','password2']