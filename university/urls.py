# Separate urls.py for each different app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ind, name='index'),
    path('<int:id>', views.view_student, name='view_student'),     #<int:id> path converted for dynamic url creation
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('fields/', views.fields_list, name='fields_list'),
    path('fields/<int:field_id>', views.field_detail, name='field_detail'),
]