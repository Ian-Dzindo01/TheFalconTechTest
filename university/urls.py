# Separate urls.py for each different app
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),     # <int:id> path converter for dynamic url creation
    path('add/', views.add, name='add'),                           
    path('edit/<int:id>', views.edit, name='edit'),                  
    path('delete/<int:id>/', views.delete, name='delete'),
    path('informaticki/', views.informaticki_view, name='informaticki'),
    path('tehnoloski/', views.tehnoloski_view, name='tehnoloski'),
    path('matematicki/', views.matematicki_view, name='matematicki')
]

# For serving media files. DEBUG should be set to false if used in production.
# Good for development, switch to Nginx or Apache for production.
if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
