from django.urls import path
from .views import *

app_name = "icecreamapp"

urlpatterns = [
    path('', variety_list, name='home'),
    path('varieties/', variety_list, name='varieties'),
    path('varieties/form', variety_form, name='variety_form'),
    path('varieties/<int:variety_id>/', variety_details, name='variety'),
      path('varieties/<int:variety_id>/form/', variety_edit_form, name='variety_edit_form'),
]
