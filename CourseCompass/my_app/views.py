from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import ModelData, LoginForm, iChairData
from django.views.decorators.csrf import csrf_exempt
import json


def home_page_view(request):
	return render(request, "home_page.html")

def catalog_page_view(request):
	data = ModelData.objects.all()
	return render(request, "catalog_page.html", {'data': data})

def complete_view(request):
	return render(request, "pending.html")

def profile_page_view(request):
	return render(request, "profile_page.html")

def settings_page_view(request):
	return render(request, "settings_page.html")

def to_do_view(request):
	return render(request, "to-do.html")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                  username=form.cleaned_data['username'], 
                  password=form.cleaned_data['password']
                  )
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request, "login.html", {"error": "Invalid credentials"})
        else:
            return render(request, "login.html", {"error": "Invalid form"})
            
    return render(request, "login_page.html")

@csrf_exempt
def receive_json(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            iChairData.objects.create(
	            termCode = data.get("term_code"),
                termNum = data.get("term_name"),
                crn = data.get("crn"),
	        )
            return JsonResponse({"status": "success"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Only POST allowed"}, status=405)

#def modelData_view(request):
#	data = ModelData.objects.all()
#	return render(request, 'catalog_page.html', {'data': data})
