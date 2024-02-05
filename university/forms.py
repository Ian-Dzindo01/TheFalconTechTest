from django import forms
from .models import Student, FieldOfStudy

# Form from creation of new students. Users first need to create a profile and only then can they apply for a specific course.
# Each user may apply only one time
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['broj', 'ime', 'prezime', 'email', 'skola', 'prosjek', 'datum', 'ocijena_mature', 'mjesto', 'molba', 'smijer', 'doc']
        labels = {
            'broj':'Broj Studenta',
            'ime':'Ime',
            'prezime':'Prezime',
            'email':'Email',
            'skola': 'Skola',
            'prosjek':'Prosijek Ocijena',
            'datum': 'Datum Rodjenja',
            'ocijena_mature': 'Ocijena na maturi',
            'mjesto': 'Mjesto rodjenja',
            'molba': 'Molba za upis',
            'smijer': 'Odaberite smijer',
            'doc': 'Dokument of zavrsenoj srednjoj skoli'
        }

        smijer = forms.ModelChoiceField(queryset=FieldOfStudy.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))    
        doc = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

        widgets = {
                'broj':forms.NumberInput(attrs={'class':'form-control'}), 
                'ime':forms.TextInput(attrs={'clas  s':'form-control'}), 
                'prezime':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'skola':forms.TextInput(attrs={'class':'form-control'}),
                'prosjek':forms.NumberInput(attrs={'class':'form-control'}),
                'datum':forms.DateInput(attrs={'class':'form-control'}),
                'ocijena_mature': forms.NumberInput(attrs={'class':'form-control'}),
                'mjesto': forms.TextInput(attrs={'class':'form-control'}),
                'molba': forms.TextInput(attrs={'class':'form-control'}),
                'doc': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }