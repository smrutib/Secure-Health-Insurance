from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser 
from django import forms 

class CustomUserCreationForm(UserCreationForm):
	npi = forms.CharField(max_length=10, required=False)
	class Meta(UserCreationForm):
		model = CustomUser
		fields=('name','username','telephone','email')
		exclude=['npi']
		


class CustomUserChangeForm(UserChangeForm):
	npi = forms.CharField(max_length=10, required=False)
	class Meta(UserChangeForm):
		model = CustomUser
		fields = ('name','username','telephone','email')
		exclude=['npi']
