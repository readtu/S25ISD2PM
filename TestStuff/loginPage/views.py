from django.shortcuts import render
from django.http import HttpResponse
from .models import loginForm

def login(request):
    if request.method == 'POST':
        #username = request.POST.get('username')
        password = request.POST.get('password')

        new_user = login(username=username, password=password)
        new_user.save()
    return render(request,'loginForm.html',{})
