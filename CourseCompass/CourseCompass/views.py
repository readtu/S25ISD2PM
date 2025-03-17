from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

#def my_view(request):
def home_page_view(request):
	return render(request, "./home_page.html")
	#template = loader.get_template('home_page.html')
	#return HttpResonse(template.render(request))
