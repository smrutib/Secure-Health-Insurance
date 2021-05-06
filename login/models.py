from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

	# add additional fields in here
	name=models.CharField(max_length=256)
	username=models.CharField(max_length=100,primary_key=True)
	password=models.CharField(max_length=100)
	telephone=models.CharField(max_length=10)
	npi=models.CharField(max_length=10, default="0000000000")
	email = models.EmailField(max_length=100)
	

