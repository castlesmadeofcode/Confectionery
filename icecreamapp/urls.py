from django.urls import path
from .views import *

app_name = "icecreamapp"

urlpatterns = [
    path('', variety_list, name='home'),
    path('varieties/', variety_list, name='varieties'),
]
