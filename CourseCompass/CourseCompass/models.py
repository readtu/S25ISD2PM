from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class Member(models.Model):
	email = models.CharField(max_length=255)

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class ModelData(models.Model):
	json_data = models.JSONField()

class iChairData(models.Model):
    termCode = models.CharField(max_length=100)
    termNum = models.CharField(max_length=100)
    crn = models.CharField(max_length=100)

