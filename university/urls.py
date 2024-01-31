# Separate urls.py for each different app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ind, name='index')
]