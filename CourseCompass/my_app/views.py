from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import LoginForm

def home_page_view(request):
	return render(request, "templates/home_page.html")

def catalog_page_view(request):
	return render(request, "templates/catelog_page.html")

def complete_view(request):
	return render(request, "templates/complete.html")

def profile_page_view(request):
	return render(request, "templates/profile_page.html")

def settings_page_view(request):
	return render(request, "templates/settings_page.html")

def to_do_view(request):
	return render(request, "templates/to-do.html")


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return JsonResponse({'success': True, 'message': 'Login successful!'}, status=200)
            else:
                return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=400)
        else:
            return JsonResponse({'success': False, 'message': 'Form is invalid'}, status=400)
    
    form = LoginForm()
    return render(request, "templates/login.html", {"form": form})
