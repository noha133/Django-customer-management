from django.forms import ModelForm
from .models import order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class OrderForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


