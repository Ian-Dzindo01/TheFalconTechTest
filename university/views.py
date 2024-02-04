from django.shortcuts import render
from .models import Student, FieldOfStudy
from .forms import StudentForm
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'university/index.html',{
        'students': Student.objects.all()})

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)                          # I don't think you are working with the actual instance here.

        if form.is_valid():
            smijer = form.cleaned_data['smijer']
            smijer_instance = FieldOfStudy.objects.get(id=smijer.id)

            if smijer_instance.student_count > smijer.quota:
                raise forms.ValidationError(f"Odabrani smijer nema vise slobodnih mjesta. Molim vas izaberite neki drugi")
            
            smijer_instance.student_count += 1
            smijer_instance.save()


            
            new_broj = form.cleaned_data['broj']
            new_ime = form.cleaned_data['prezime']
            new_prezime = form.cleaned_data['ime']
            new_email = form.cleaned_data['email']
            new_skola = form.cleaned_data['skola']
            new_prosjek = form.cleaned_data['prosjek']
            new_datum = form.cleaned_data['datum']
            new_ocijena_mature = form.cleaned_data['ocijena_mature']
            new_mjesto = form.cleaned_data['mjesto']
            new_molba = form.cleaned_data['molba']
            new_smijer = smijer

            newStudent = Student(              # Add document upload support here.
                broj = new_broj,
                ime = new_ime,
                prezime = new_prezime,
                email = new_email,
                skola = new_skola,
                prosjek = new_prosjek,
                datum = new_datum, 
                ocijena_mature = new_ocijena_mature,
                mjesto = new_mjesto,
                molba = new_molba,
                smijer=new_smijer,
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

def informaticki_view(request):
    informaticki_instance = FieldOfStudy.objects.get(name='Informaticki')
    student_count = informaticki_instance.student_count
    subjects = ['Programming', 'Database Management', 'Web Development']
    plan_of_study = 'Informaticki Plan of Study: ...'
    return render(request, 'university/field_of_study.html', {'field': 'Informaticki', 'subjects': subjects, 'plan_of_study': plan_of_study, 'cnt': student_count})

def tehnoloski_view(request):
    tehnoloski_instance = FieldOfStudy.objects.get(name='Tehnoloski')
    student_count = tehnoloski_instance.student_count
    subjects = ['Engineering', 'Robotics', 'Automation']
    plan_of_study = 'Tehnoloski Plan of Study: ...'
    return render(request, 'university/field_of_study.html', {'field': 'Tehnoloski', 'subjects': subjects, 'plan_of_study': plan_of_study, 'cnt': student_count})

def matematicki_view(request):
    matematicki_instance = FieldOfStudy.objects.get(name='Matematicki')
    student_count = matematicki_instance.student_count
    subjects = ['Calculus', 'Linear Algebra', 'Statistics']
    plan_of_study = 'Matematicki Plan of Study: ...'
    return render(request, 'university/field_of_study.html', {'field': 'Matematicki', 'subjects': subjects, 'plan_of_study': plan_of_study, 'cnt': student_count})

