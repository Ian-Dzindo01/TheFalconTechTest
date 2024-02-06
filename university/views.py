from django.shortcuts import render, redirect
from .models import Student, FieldOfStudy
from .forms import StudentForm
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Index page
def index(request, **kwargs):
    # Get the username and email from the query parameters
    fromadd = request.GET.get('fromadd', False)
    success = request.GET.get('success', False)
    username = request.GET.get('username', '')  
    email = request.GET.get('email', '')

    # Check if a student with the same email exists in the database
    # Used to determine whether register button is shown again
    # Room for improvement in this logic
    if fromadd:
        student_exists = True
    else:
        student_exists = Student.objects.filter(email=email).exists() 

    print('DOES STUDENT EXIST:', student_exists)           
                                                                             
    context = {
        'username': username,
        'students': Student.objects.all(),
        'student_exists': student_exists,
    }

    return render(request, 'university/index.html', context)

# Main login page
def login_view(request):
    return render(request, 'university/login.html')

def view_student(request, id):
    # Get student data by id
    student = Student.objects.get(pk=id)                         

    # Redirect to home page
    return HttpResponseRedirect(reverse('index'))                

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)                          

        if form.is_valid():
            smijer = form.cleaned_data['smijer']
            smijer_instance = FieldOfStudy.objects.get(id=smijer.id)

            # Check if there is available seats in the selected course 
            if smijer_instance.student_count > smijer.quota:
                raise forms.ValidationError(f"Odabrani smijer nema vise slobodnih mjesta. Molim vas izaberite neki drugi")
            
            # Increment number of students in selected course
            smijer_instance.student_count += 1
            smijer_instance.save()
            
            # Make sure data is in right format
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
            new_doc = form.cleaned_data['doc']

            newStudent = Student(              
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
                doc=new_doc
            )   

            newStudent.save()
            
            fromadd = True
            # Redirect to the index page after successful submission
            redirect_url = reverse('index') + f'?fromadd={fromadd}'
            return redirect(redirect_url) 
    else:
        # Display an empty form for GET requests
        form = StudentForm()

    return render(request, 'university/add.html', {'form': form})


# Edit student specific data
def edit(request, id):

    # Get student by id
    student = Student.objects.get(pk=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return render(request, 'university/edit.html', {
                'form': form,
                'success': True
            })
    # If method is GET
    else:
        form = StudentForm(instance=student)

    return render(request, 'university/edit.html', {
        'form': form
    })

# Delete a specific student
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    # Redirect to index
    return HttpResponseRedirect(reverse('index'))

# Specific field of study view functions
def informaticki_view(request):
    # Each of these have to be instantiated in the shell. Code on github README
    informaticki_instance = FieldOfStudy.objects.get(name='Informaticki')
    # student_count passed to html file for display
    student_count = informaticki_instance.student_count
    # Random course data
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

