from django.shortcuts import render
from login.models import CustomUser
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from login import forms
from .forms import CustomUserCreationForm
from django.views.generic import View
from django.shortcuts import redirect

def home(request):
	return render(request,"login/home.html")

def signin(request):
	
	return render(request,"registration/login.html")

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'login/signup.html'

	def form_valid(self,form):
		if form.cleaned_data['npi']:
			npi=form.cleaned_data['npi']
		else:
			npi='0000000000'
		print(npi)
		form.instance.npi=npi
		return super().form_valid(form)

def login_success(request):
	npi=request.user.npi
	if npi== "0000000000":
		return redirect("/analysis/index")
	else:
		return redirect("/analysis/provider")
	

