from django.urls import path
from .views import home, receive_data

urlpatterns = [
    path('', home, name='home'),
    path('data/', receive_data, name='receive_data'),
]
