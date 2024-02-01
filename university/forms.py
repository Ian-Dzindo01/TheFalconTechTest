from django import forms
from .models import students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['number', 'fName', 'lName', 'email', 'smijerOdab', 'prosjekOc']
        labels = {
            'number':'Student Number',
            'fName':'First Name',
            'lName':'Last Name',
            'email':'Email',
            'smijerOdab':'Smijer',
            'prosjekOc':'Prosijek Ocijena'
        }
        widgets = {
                'number':forms.NumberInput(attrs={'class':'form-control'}), 
                'fName':forms.TextInput(attrs={'class':'form-control'}), 
                'lName':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'smijerOdab':forms.TextInput(attrs={'class':'form-control'}),
                'prosjekOc':forms.NumberInput(attrs={'class':'form-control'})
                }