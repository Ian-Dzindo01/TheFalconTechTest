from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.urls import reverse


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = authenticate(username=request.data['username'], password=request.data['password'])
            refresh = RefreshToken.for_user(user)
            response.data['refresh'] = str(refresh)
            response.data['access'] = str(refresh.access_token)

            redirect_url = reverse('index') + f'?username={user.username}'
            
            response.data['redirect'] = redirect_url
            return redirect(redirect_url)  # Redirect the user immediately after login
        
        return response

class HelloView(APIView):
    def get(self, request):
        return Response(data={"message": "Hello, you are authenticated!"}, status=status.HTTP_200_OK)
    
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'university/login.html', {'form': form})