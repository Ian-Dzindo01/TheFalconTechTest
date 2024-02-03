from django.shortcuts import render, get_object_or_404
from .models import Student
from .forms import StudentForm
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
        form = StudentForm(request.POST)
        if form.is_valid():
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
            new_smijer = form.cleaned_data['smijer']
            # new_doc = form.cleaned_data['doc']

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
                # doc = new_doc
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