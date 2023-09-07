from django.urls import path
from . import views

urlpatterns = [
    # ...other URL patterns...
    path('api/deposit/', views.initiate_deposit, name='initiate-deposit'),
]
