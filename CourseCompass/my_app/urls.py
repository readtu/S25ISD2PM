from django.urls import path
from .views import home
from .views import receive_data

urlpatterns = [
    path('data/', receive_data, name='receive_data'),
    path('', home, name='home'),
]

