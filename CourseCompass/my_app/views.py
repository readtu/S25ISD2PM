from django.http import HttpRepsonse
from django.template import loader
from django.shortcuts import render

def home_page_view(request):
	return render(request, "templates/home_page.html")
# Create your views here.
