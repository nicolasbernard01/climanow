from django.urls import path
from . import views

urlpatterns = [
    path('', views.clima, name='clima'),
    
]