from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from .views import login_view
from .views import receive_json

urlpatterns = [
    path("", views.home_page_view, name="home"),
    path("home_page.html/", views.home_page_view, name="home"),
    path("catalog_page.html/", views.catalog_page_view, name="catalog"),
    path("pending.html/", views.complete_view, name="pending"),
    path("profile_page.html/", views.profile_page_view, name="profile_page"),
    path("settings_page.html/", views.settings_page_view, name="settings"),
    path("to-do.html/", views.to_do_view, name="to-do"),
    path("login_page.html/", views.login_view, name="login"),
    path("api/receive/", receive_json, name="receive_json"),
]