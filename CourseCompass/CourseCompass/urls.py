"""
URL configuration for CourseCompass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path("", views.home_page_view, name="home"),
    path("home_page.html/", views.home_page_view, name="home"), #admin.site.urls),
	path("catalog_page.html/", views.catalog_page_view, name="catalog"),
	path("complete.html/", views.complete_view, name="complete"),
	path("profile_page.html/", views.profile_page_view, name="profile_page"),
	path("settings_page.html/", views.settings_page_view, name="settings"),
	path("to-do.html/", views.to_do_view, name="to-do"),
	path("login_page.html/", views.login_view, name="login"),

]

#urlpatterns = [
#	path("my_app/", include("my_app.urls")),
#]

