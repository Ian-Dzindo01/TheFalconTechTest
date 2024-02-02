from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['number', 'fName', 'lName', 'email', 'smijerOdab', 'prosjekOc', 'datumRodj', 'maturaOc', 'mjestoRodj', 'molba', 'doc']
        labels = {
            'number':'Student Number',
            'fName':'First Name',
            'lName':'Last Name',
            'email':'Email',
            'smijerOdab':'Smijer',
            'prosjekOc':'Prosijek Ocijena',
            'datumRodj': 'Datum Rodjenja',
            'maturaOc': 'Ocijena na maturi',
            'mjestoRodj': 'Mijesto rodjenja',
            'molba': 'Molba za upis',
            'doc': 'Dokument o zavrsenoj srednjoj skoli'

        }
        widgets = {
                'number':forms.NumberInput(attrs={'class':'form-control'}), 
                'fName':forms.TextInput(attrs={'class':'form-control'}), 
                'lName':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'smijerOdab':forms.TextInput(attrs={'class':'form-control'}),
                'prosjekOc':forms.NumberInput(attrs={'class':'form-control'}),
                'datumRodj':forms.DateInput(attrs={'class':'form-control'}),
                'maturaOc': forms.NumberInput(attrs={'class':'form-control'}),
                'mjestoRodj': forms.TextInput(attrs={'class':'form-control'}),
                'molba': forms.TextInput(attrs={'class':'form-control'}),
                'doc': forms.FileInput(attrs={'class': 'form-control'})
                }