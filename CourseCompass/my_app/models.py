from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Create your models here.
class Member(models.Model):
  email = models.CharField(max_length=255)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
  
