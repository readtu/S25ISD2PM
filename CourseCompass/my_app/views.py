from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.utils.html import format_html
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .templatetags.custom_tags import grab_data
import json
import logging

logger = logging.getLogger(__name__)

def home_page_view(request):
	return render(request, "home_page.html")

def catalog_page_view(request):
	data = ModelData.objects.all()
	html_string = grab_data(data)
	output = {'html_string': format_html(html_string)}
	return render(request, "catalog_page.html", output) #{'data': data})

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
    # Initial logging
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.error("This is an error message")

    # Create a test object
    obj = iChairData.objects.create(
        termCode="TESTTERM",
        termNum="TESTNUM",
        crn="12345"
    )
    print("Created object ID:", obj.id)

    # Only accept POST
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received JSON:", data)

            # Create from incoming payload
            iChairData.objects.create(
                termCode=data.get("term_code"),
                termNum=data.get("term_name"),
                crn=data.get("crn"),
            )

            # Example hard-coded entry
            iChairData.objects.create(
                termCode="123",
                termNum="456",
                crn="789",
            )

            return JsonResponse({"status": "success"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    # If not POST, return an error
    return JsonResponse({"error": "Only POST allowed"}, status=405)

#def modelData_view(request):
#	data = ModelData.objects.all()
#	return render(request, 'catalog_page.html', {'data': data})
