from django.shortcuts import render
from .models import Student

def ind(request):
    return render(request, 'university/index.html',{
        'students': Student.objects.all()})