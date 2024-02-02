from django.shortcuts import render, get_object_or_404
from .models import Student, FieldOfStudy
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

def edit(request, id):
    student = Student.objects.get(pk=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'university/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)

    return render(request, 'university/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))

def fields_list(request):
    fields = FieldOfStudy.objects.all()
    return render(request, 'fields/fields_list.html', {'fields':fields})

def field_detail(request, field_id):
    field = get_object_or_404(FieldOfStudy, pk=field_id)
    return render(request, 'fields/field_detail.html', {'field':field})

