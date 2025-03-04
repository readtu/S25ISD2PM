from django.hppt import HttpResponse
from django.template import loader

def my_view(request):
	template = loader.get_template('home_page.html')
	return HttpResonse(template.render(request))
