# Separate urls.py for each different app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ind, name='index'),
    path('<int:id>', views.view_student, name='view_student')     #<int:id> path converted for dynamic url creation
]