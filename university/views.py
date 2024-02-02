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
            new_number = form.cleaned_data['number']
            new_fname = form.cleaned_data['fName']
            new_lname = form.cleaned_data['lName']
            new_email = form.cleaned_data['email']
            new_smijer = form.cleaned_data['smijerOdab']
            new_prosjek = form.cleaned_data['prosjekOc']
            new_maturaOc = form.cleaned_data['maturaOc']
            new_mjestoRodj = form.cleaned_data['mjestoRodj']
            new_molba = form.cleaned_data['molba']

            newStudent = Student(
                number=new_number,
                fName=new_fname,
                lName=new_lname,
                email=new_email,
                smijerOdab=new_smijer,
                prosjekOc=new_prosjek,
                maturaOc = new_maturaOc,
                mjestoRodj = new_mjestoRodj,
                molba = new_molba
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

