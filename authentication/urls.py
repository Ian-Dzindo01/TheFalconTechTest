from django.urls import path
from .views import CustomTokenObtainPairView, HelloView, registration_view

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('register/', registration_view, name='register')  # Add registration URL
]