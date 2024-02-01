from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def ind(request):
    return render(request, 'university/index.html',{
        'students': Student.objects.all()})

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new1 = form.cleaned_data['number']
            new2 = form.cleaned_data['fName']
            new3 = form.cleaned_data['lName']
            new4 = form.cleaned_data['email']
            new5 = form.cleaned_data['smijerOdab']
            new6 = form.cleaned_data['prosjekOc']

            newStudent = Student(
                number=new1,
                fName=new2,
                lName=new3,
                email=new4,
                smijerOdab=new5,
                prosjekOc=new6
            )
            newStudent.save()
            
            # Redirect to the index page after successful submission
            return render(request, 'university/add.html', {
                'form':StudentForm(),
                'success':True
            })
    else:
        # Display an empty form for GET requests
        form = StudentForm()

    return render(request, 'university/add.html', {
        'form': form
    })