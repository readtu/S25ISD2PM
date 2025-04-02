from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import LoginForm


def catalog_page_view(request):
	return render(request, "catalog_page.html")

def complete_view(request):
	return render(request, "complete.html")

def profile_page_view(request):
	return render(request, "profile_page.html")

def settings_page_view(request):
	return render(request, "settings_page.html")

def to_do_view(request):
	return render(request, "to-do.html")

def home_page_view(request):
	return render(request, "home_page.html")

def login_view(request):
	if request.method == "POST":
		form = LoginForm(data=request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user:
				login(request, user)
			else:
				return JsonResponse({'success': False, 'message': 'Form is invalid'}, status=400)
		else:
			return JsonResponse({'success': False, 'message': 'Form is invalid'}, status=400)
	form = LoginForm()
	return render(request, "login.html", {"form": form})
