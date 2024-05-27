from django import forms
from .models import *

class CustomerDetailForm(forms.ModelForm):
    class Meta:
        model = customer_details
        fields = ['first_name', 'username', 'password', 'email']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'music', 'image', 'video', 'camera_image']

class UserInfoFrom(forms.ModelForm):
    class Meta:
        model = User_info
        fields = ['first_name', 'last_name', 'e_mail', 'Mobno','birth_date','gender', 'city', 'message']