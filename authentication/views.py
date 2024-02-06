from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.urls import reverse

# JWT Authentication and Login function
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Call post method of parent class, pass in request as argument
        response = super().post(request, *args, **kwargs)  
        if response.status_code == 200:
            # Authenticate user with credentials
            user = authenticate(username=request.data['username'], password=request.data['password'])
            # Refresh token used to obtain new access tokens without requiring credential reentering. Stored in response.
            refresh = RefreshToken.for_user(user)
            response.data['refresh'] = str(refresh)
            # Store access token in response
            response.data['access'] = str(refresh.access_token)

            # Specify where to redirect and pass username and email to receiver. Used for output in index.html
            redirect_url = reverse('index') + f'?username={user.username}&email={user.email}'
            response.data['redirect'] = redirect_url

            # For login_required redirect. Grabs the path from the next variable in the url and redirects to it after login.
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # Redirect the user immediately after login
                return redirect(redirect_url)  
        
        return response

class HelloView(APIView):
    def get(self, request):
        return Response(data={"message": "Hello, you are authenticated!"}, status=status.HTTP_200_OK)
    
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after successful registration
            return redirect('login')  
    else:
        form = RegistrationForm()

    return render(request, 'university/login.html', {'form': form})